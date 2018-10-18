import csv
from .vertex_edge import Vertex, Edge


def parse_node_data(filename: str):
    """
    Reads a csv file containing data about the nodes.
    This file's first column must be the id of a node (a integer from 0 to N)

    Returns:
    The list of Vertex objects L where L[i] is the object of id i.
    """
    assert ".csv" in filename
    output = []
    with open(filename, "r") as csvfile:
        reader = list(csv.reader(csvfile, delimiter=','))
        header = [x.strip().split(')')[0].split('(') for x in reader[0]]
        for row in reader[1:]:
            d = dict()
            for i in range(len(row)):
                name, t = header[i]
                if t == "STR":
                    d[name] = row[i]
                elif t == "FLOAT":
                    d[name] = float(row[i])
                elif t == "INT":
                    d[name] = int(row[i])
                elif t == "BOOL":
                    d[name] = bool(row[i])
                else:
                    raise Exception("Unknown data type: "+str(t))
            output.append(Vertex(d["id"], d))
    return output


def write_node_data(filename: str) -> None:
    return


def parse_edge_data(filename: str, oriented: bool = True):
    assert ".csv" in filename
    output = dict()
    with open(filename, "r") as csvfile:
        reader = list(csv.reader(csvfile, delimiter=','))
        header = [x.strip().split(')')[0].split('(') for x in reader[0]]
        for row in reader[1:]:
            d = dict()
            for i in range(len(row)):
                name, t = header[i]
                if t == "STR":
                    d[name] = row[i]
                elif t == "FLOAT":
                    d[name] = float(row[i])
                elif t == "INT":
                    d[name] = int(row[i])
                elif t == "BOOL":
                    d[name] = bool(row[i])
                else:
                    raise Exception("Unknown data type: "+str(t))
            if (d["start"], d["end"]) not in output:
                output[(d["start"], d["end"])] = [
                    Edge(oriented=oriented, data=d)]
            else:
                output[(d["start"], d["end"])].append(
                    Edge(oriented=oriented, data=d))

    return output


def write_edge_data(filename: str) -> None:
    return
