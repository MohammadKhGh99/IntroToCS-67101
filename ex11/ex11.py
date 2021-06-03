import itertools

class Node:
    def __init__(self, data, pos=None, neg=None):
        self.data = data
        self.positive_child = pos
        self.negative_child = neg


class Record:
    def __init__(self, illness, symptoms):
        self.illness = illness
        self.symptoms = symptoms


def parse_data(filepath):
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    def __init__(self, root):
        self.root = root

    def diagnose(self, symptoms):
        """
        this function diagnose what illness does the symptoms lead to
        :param symptoms: the symptoms
        :return: returns the leaf (illness) that the symptoms lead to
        """
        new_root = self.root
        pos = new_root.positive_child
        while pos is not None:
            if new_root.data in symptoms:
                new_root = new_root.positive_child
            else:
                new_root = new_root.negative_child
            pos = new_root.positive_child
        return new_root.data

    def calculate_success_rate(self, records):
        """
        this function calculate the rate of the success of finding an
        illness in the records
        :param records: the records
        :return: returns the rate
        """
        length = len(records)
        success_counter = 0
        for record in records:
            diagnose = self.diagnose(record.symptoms)
            if diagnose == record.illness:
                success_counter += 1
        rate = success_counter / length
        return rate

    def all_illnesses_helper(self, node, illnesses):
        """
        this function takes all the illnesses
        :param node: the root of the tree
        :param illnesses: all the illnesses
        :return: returns a dictionary with the illnesses
        """
        illness = node.data
        if node.positive_child is None:
            if illness not in illnesses:
                illnesses.update({
                    illness: 1})
            else:
                illnesses[illness] += 1
        else:
            self.all_illnesses_helper(node.positive_child, illnesses)
            self.all_illnesses_helper(node.negative_child, illnesses)
        return illnesses

    def convert_dict_to_list(self):
        """
        this function converts the dictionary to sorted list by the value of
        every key in the dictionary.
        :return: returns a sorted list
        """
        lst = self.all_illnesses_helper(self.root, {})
        a = [(v, k) for k, v in lst.items()]
        a = sorted(a)
        illnesses = {}
        for i in range(len(a)):
            illnesses.update({a[i][1]: a[i][0]})
        return list(illnesses)

    def all_illnesses(self):
        """
        this function takes all the illnesses and sort them by their value
        :return: returns a sorted list of illnesses
        """
        illnesses = self.convert_dict_to_list()
        illnesses = illnesses[::-1]
        return illnesses

    def most_rare_illness_helper(self, symptoms, node, illnesses):
        """
        this function checks how much times we arrived to illness
        :param symptoms: the symptom of the current record
        :param node: the root
        :param illnesses: dictionary of illnesses
        :return: returns dictionary
        """
        if node.positive_child is None:
            if node.data not in illnesses:
                illnesses.update({node.data: 1})
            else:
                illnesses[node.data] += 1
        else:
            if node.data in symptoms:
                node = node.positive_child
                self.most_rare_illness_helper(symptoms, node, illnesses)
            else:
                node = node.negative_child
                self.most_rare_illness_helper(symptoms, node, illnesses)
        return illnesses

    def most_rare_illness(self, records):
        """
        this function checks the less illness that we arrived
        :param records: the records to check with
        :return: returns the less illness that we arrived to by the records
        """
        illnesses = {}
        for record in records:
            illnesses.update(self.most_rare_illness_helper(record.symptoms,
                                                        self.root,illnesses))
        illnesses = self.convert_dict_to_list()
        return illnesses[0]

    def paths_to_illness_helper(self, illness, node, single_path, all_paths):
        """
        this function find all the paths for an illness
        :param illness: the chosen illness
        :param node: the root of the tree
        :param single_path: one single path
        :param all_paths: all the paths of the illness
        :return: returns None
        """
        pos = node.positive_child
        neg = node.negative_child
        if pos is None:
            if node.data == illness:
                all_paths.append(single_path[:])
                return
        else:
            single_path.append(True)
            self.paths_to_illness_helper(illness, pos, single_path, all_paths)
            single_path.pop()
            single_path.append(False)
            self.paths_to_illness_helper(illness, neg, single_path, all_paths)
            single_path.pop()

    def paths_to_illness(self, illness):
        """
        this function finds all the paths for an illness
        :param illness: the chisen illness
        :return: return a list of lists of the paths
        """
        all_paths_list = []
        self.paths_to_illness_helper(illness, self.root, [], all_paths_list)
        return all_paths_list


def build_tree_with_symptoms(symptoms, node, i):
    if i == len(symptoms):
        return
    else:
        for j in range(i * 2):
            node.positive_child = Node(symptoms[i])
            node.negative_child = Node(symptoms[i])
        i += 1
        build_tree_with_symptoms(symptoms, node.positive_child, i)
        build_tree_with_symptoms(symptoms, node.negative_child,i)


def func(node, pos_lst, neg_lst, records, father):
    if node is not None:
        func(node.positive_child, pos_lst + [node.data], neg_lst, records, node)
        func(node.negative_child, pos_lst, neg_lst + [node.data], records, node)
    else:
        dic = {}
        for record in records:
            flag = True
            for pos in pos_lst:
                if pos not in record.symptoms:
                    flag = False
                    break

            for neg in neg_lst:
                if neg in record.symptoms:
                    flag = False
                    break

            if flag:
                if record.illness not in dic:
                    dic[record.illness] = 1
                else:
                    dic[record.illness] += 1

        # if we didn't get anything for this location from records
        if len(dic) == 0:
            ill_lst = [records[0].illness]
        else:
            # organizing the dictionary and converting it to list
            a = [(v, k) for k, v in dic.items()]
            a = sorted(a,reverse=True)
            illnesses = {}
            for i in range(len(a)):
                illnesses.update({
                    a[i][1]: a[i][0]})
            ill_lst = list(illnesses)

        if father.data in pos_lst:
            father.positive_child = Node(ill_lst[0])
        else:
            father.negative_child = Node(ill_lst[0])


def build_tree(records, symptoms):
    tree_root = Node(symptoms[0])
    node = tree_root
    build_tree_with_symptoms(symptoms, tree_root, 1)
    func(node, [], [], records, node)
    return node


def optimal_tree(records, symptoms, depth):
    """
    this function takes all the subsets of the symptoms at depth length and
    build a tree from each list theen takes the tree with the bigger succes
    rate of one of thtrees
    :param records: list of records
    :param symptoms: list of symptoms
    :param depth: the depth of the trees
    :return: returns the tree (Node) that her success rate is the bigger
    from the others
    """
    trees_dict={}
    for symptom_list in itertools.combinations(symptoms,depth):
        tree=build_tree(records,symptom_list)
        diagnoser=Diagnoser(tree)
        rate=diagnoser.calculate_success_rate(records)
        trees_dict[tree]=rate
    list_of_tuples = [(k,v) for k, v in trees_dict.items()]
    list_of_tuples = sorted(list_of_tuples,key=lambda tup:tup[1])
    list_of_tuples=list_of_tuples[::-1]
    return list_of_tuples[0][0]

if __name__ == "__main__":

    # Manually build a simple tree.
    #                cough
    #          Yes /       \ No
    #        fever           healthy
    #   Yes /     \ No
    # influenza   cold
    pass
    flu_leaf = Node("influenza", None, None)
    cold_leaf = Node("cold", None, None)
    inner_vertex = Node("fever", flu_leaf, cold_leaf)
    healthy_leaf = Node("healthy", None, None)
    root = Node("cough", inner_vertex, healthy_leaf)

    diagnoser = Diagnoser(root)

    # Simple test
    diagnosis = diagnoser.diagnose(["cough"])
    if diagnosis == "cold":
        print("Test passed")
    else:
        print("Test failed. Should have printed cold, printed: ", diagnosis)

# Add more tests for sections 2-7 here.
