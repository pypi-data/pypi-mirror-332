import os
from logging import getLogger
from pathlib import Path

import pandas
from anytree import Node, RenderTree

from ._mapping_type import get_comment, skos_uri_dict

logger = getLogger("root")

ROOT_PATH = Path(os.path.dirname(__file__))

activitytype_path = "data/flow/activitytype/"
location_path = "data/location/"
dataquality_path = "data/dataquality/"
unit_path = "data/unit/"
uncertainty_path = "data/uncertainty/"
time_path = "data/time/"
flowobject_path = "data/flow/flowobject/"
flow_path = "data/flow/"

# Lookup function for pandas DataFrame
def lookup(self, keyword):
    """Filter the DataFrame based on the keyword in the "name" column"""
    filtered_df = self[self["name"].str.contains(keyword)]
    return filtered_df


def get_children(
    self, parent_codes, deep=True, return_parent=False, exclude_sut_children=False
):
    """
    Get descendants (direct and indirect) for a list of parent_codes.

    Argument
    --------
    parent_codes: list or str
         A single parent_code or a list of parent_codes for which descendants are to be fetched.
    deep : bool
        True to include all descendants, False to include only direct children.
    return_parent: bool
        True to include the parent codes in the returned dataframe, default is False
    exclude_sut_children: bool
        True if the parent code is considerred as a code in the final Bonsai SUTs.
        If True, only the children of the parent code are returned that are NOT in the SUT.

    Returns
    -------
    pandas.DataFrame
        Tree table containing rows with descendants of the specified parent_codes.
    """
    if not isinstance(self, pandas.DataFrame):
        raise TypeError("The object must be a pandas DataFrame.")

    if not {"code", "parent_code"}.issubset(self.columns):
        raise KeyError("Data table must have 'code' and 'parent_code' columns.")

    if isinstance(parent_codes, str):
        parent_codes = [parent_codes]
    elif not isinstance(parent_codes, (list, set, tuple)):
        raise TypeError("parent_codes must be a string or a list-like object")

    if exclude_sut_children:
        if "in_final_sut" in self.columns:
            bonsai_codes = self[self["in_final_sut"] == "True"]["code"]
        else:
            bonsai_codes = []

    if deep == True:
        to_explore = set(parent_codes)
        all_descendants = set()

        while to_explore:
            current_children = self[self["parent_code"].isin(to_explore)]

            new_descendants = set(current_children["code"])
            if exclude_sut_children is True:
                new_descendants = new_descendants - set(bonsai_codes)
            all_descendants.update(new_descendants)

            to_explore = new_descendants - all_descendants.union(to_explore)
            to_explore.update(new_descendants)
        if len(all_descendants) == 0:
            all_descendants = parent_codes
            logger.warning(f"no children found for {parent_codes}")

        df = self[self["code"].isin(all_descendants)]
    elif deep == False:
        if not self[self["parent_code"].isin(parent_codes)].empty:
            df = self[self["parent_code"].isin(parent_codes)]
        else:
            df = self[self["code"].isin(parent_codes)]
    df = df[df.code.isin(parent_codes) == False]
    if return_parent == True:
        df_p = self[self["code"].isin(parent_codes)]
        df = pandas.concat([df_p, df])
    return df


def create_conc(df_A, df_B, source="", target=""):
    """Create new concordance based on two other tables.

    Argument
    --------
    df_A : pandas.DataFrame
        concordance table A
        with mapping from "x" to "y"
    df_B : pandas.DataFrame
        concordance table B
        with mapping from "y" to "z"
    target : str
        classification name that specifies "x"
    source : str
        classification name that specifies "z"

    Returns
    -------
    pandas.DataFrame
        concordance table with mapping form "x" to "z"
    """
    if "activitytype_to" in df_B.columns and "flowobjet_to" in df_B.columns:
        raise NotImplementedError("Concpair tables not allowed")
    if "activitytype_to" in df_A.columns and "activitytype_to" in df_B.columns:
        column_prefix = "activitytype"
    if "flowobject_to" in df_A.columns and "flowobject_to" in df_B.columns:
        column_prefix = "flowobject"

    merged = pandas.merge(df_A, df_B, on=f"{column_prefix}_to", suffixes=("_A", "_B"))

    # Create the resulting DataFrame with required columns
    result = pandas.DataFrame(
        {
            f"{column_prefix}_from": merged[f"{column_prefix}_from_A"],
            f"{column_prefix}_to": merged[f"{column_prefix}_from_B"],
            "classification_from": source,  # Fixed value from A
            "classification_to": target,  # Fixed value for result
        }
    )

    # Drop duplicate pairs of source and target
    new_mapping = result.drop_duplicates(
        subset=[
            f"{column_prefix}_from",
            f"{column_prefix}_to",
            "classification_from",
            "classification_to",
        ]
    )

    # Calculate the counts of each source and target in the merged DataFrame
    source_counts = new_mapping[f"{column_prefix}_from"].value_counts().to_dict()
    target_counts = new_mapping[f"{column_prefix}_to"].value_counts().to_dict()
    # Apply the get_comment function to each row
    new_mapping["comment"] = new_mapping.apply(
        lambda row: get_comment(
            source_counts[row[f"{column_prefix}_from"]],
            target_counts[row[f"{column_prefix}_to"]],
            s=row[f"{column_prefix}_from"],
            t=row[f"{column_prefix}_to"],
        ),
        axis=1,
    )
    new_mapping["skos_uri"] = new_mapping["comment"].map(skos_uri_dict)

    new_mapping = new_mapping[
        [
            f"{column_prefix}_from",
            f"{column_prefix}_to",
            "classification_from",
            "classification_to",
            "comment",
            "skos_uri",
        ]
    ]
    new_mapping = new_mapping.reset_index(drop=True)
    return new_mapping


def _get_concordance_file(file_path):
    try:
        # Read the concordance CSV into a DataFrame
        return pandas.read_csv(file_path, dtype=str)
        # return multiple_dfs
    except FileNotFoundError:
        return None
    except Exception as e:
        logger.error(f"Error reading concordance file: {e}")
        return None


def get_concordance(from_classification, to_classification):
    """
    Get the concordance DataFrame based on the specified classifications.
    Parameters
    ----------
    from_classification: str
        The source classification name (e.g., "bonsai").
    to_classification: str
        The target classification name (e.g., "nace_rev2").
    Returns
    -------
    pd.DataFrame
        The concordance DataFrame if 1 file is found; otherwise, a dict of DataFrames.
    """
    # Construct the file name
    fitting_file_names = [
        f"conc_{from_classification}_{to_classification}.csv",
        f"concpair_{from_classification}_{to_classification}.csv",
    ]
    reversed_file_names = [
        f"conc_{to_classification}_{from_classification}.csv",
        f"concpair_{to_classification}_{from_classification}.csv",
    ]
    file_paths = [
        activitytype_path,
        location_path,
        dataquality_path,
        unit_path,
        uncertainty_path,
        time_path,
        flowobject_path,
        flow_path,
    ]
    multiple_dfs = {}
    for f in file_paths:
        for n in fitting_file_names:
            file_path = ROOT_PATH.joinpath(f, n)
            df = _get_concordance_file(file_path)
            if not df is None:
                multiple_dfs[f"{f}"] = df
        for n in reversed_file_names:
            file_path = ROOT_PATH.joinpath(f, n)
            df = _get_concordance_file(file_path)
            if not df is None:
                # Renaming columns
                new_columns = {}
                for col in df.columns:
                    if "_from" in col:
                        new_columns[col] = col.replace("_from", "_to")
                    elif "_to" in col:
                        new_columns[col] = col.replace("_to", "_from")
                df.rename(columns=new_columns, inplace=True)

                # Changing the comment column
                df["comment"] = df["comment"].replace(
                    {
                        "one-to-many correspondence": "many-to-one correspondence",
                        "many-to-one correspondence": "one-to-many correspondence",
                    }
                )
                df["skos_uri"] = df["skos_uri"].replace(
                    {
                        "http://www.w3.org/2004/02/skos/core#narrowMatch": "http://www.w3.org/2004/02/skos/core#broadMatch",
                        "http://www.w3.org/2004/02/skos/core#broadMatch": "http://www.w3.org/2004/02/skos/core#narrowMatch",
                    }
                )
                multiple_dfs[f"{f}"] = df

    if len(multiple_dfs):
        return multiple_dfs[next(iter(multiple_dfs))]
    else:
        return multiple_dfs


def print_tree(self, toplevelcode):
    """Print the tree structure for a given code.

    Bold text represent sub-categories which are included when applying it in the Bonsai SUT.
    Italic text represent sub-categories which are not included, since these are separate codes in the Bonsai SUT.

    """
    all_codes = self.get_children(
        toplevelcode, deep=True, return_parent=True, exclude_sut_children=False
    )
    sut_codes = self.get_children(
        toplevelcode, deep=True, return_parent=True, exclude_sut_children=True
    )
    # Create nodes from the data
    nodes = {}
    for _, row in all_codes.iterrows():
        nodes[row["code"]] = Node(
            row["code"], parent=nodes.get(row["parent_code"]), descript=row["name"]
        )

    italic_codes = set(sut_codes["code"])  # Set of codes to make italic
    for pre, fill, node in RenderTree(nodes[toplevelcode]):
        if node.name in italic_codes:
            print(f"{pre}\033[1m{node.name} - {node.descript}\033[0m")  # Italicize text
        else:
            print(f"{pre}\033[3m{node.name} - {node.descript}\033[0m")


# Subclass pandas DataFrame
class CustomDataFrame(pandas.DataFrame):
    lookup = lookup
    get_children = get_children
    print_tree = print_tree
