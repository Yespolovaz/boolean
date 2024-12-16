# import tkinter as tk
# from tkinter import ttk, messagebox
from typing import Callable
from itertools import product

# class QuineMcCluskeyGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Quine-McCluskey Minimization")

#         # Input Label and Entry
#         self.label = ttk.Label(root, text="Enter Minterms (space-separated):")
#         self.label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

#         self.minterm_entry = ttk.Entry(root, width=50)
#         self.minterm_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

#         # Process Button
#         self.process_button = ttk.Button(root, text="Process", command=self.process_minterms)
#         self.process_button.grid(row=1, column=0, columnspan=2, pady=10)

#         self.clear_button = ttk.Button(root, text="Clear", command=self.clear_fields)
#         self.clear_button.grid(row=3, column=0, columnspan=2, pady=10)

#         # Output Text Box
#         self.output_text = tk.Text(root, width=80, height=30, wrap=tk.WORD)
#         self.output_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

#     def process_minterms(self):
#         minterms = self.minterm_entry.get()
#         try:
#             qm = QuineMcCluskey(minterms)
#             output = qm.table()
#             self.output_text.delete(1.0, tk.END)
#             self.output_text.insert(tk.END, output)
#         except Exception as e:
#             messagebox.showerror("Error", f"Invalid input: {e}")

#     def clear_fields(self):
#         self.minterm_entry.delete(0, tk.END)
#         self.output_text.delete(1.0, tk.END)


class QuineMcCluskey:
    def __init__(self, minterms):
        minterms = minterms.strip().split(' ')
        minterms = list(map(int, minterms))
        minterms.sort()
        self.minterms = minterms
        self.size = len(bin(self.minterms[-1]))-2
        self.groups = {}
        self.all_pi = set()
        self.chart = {}

    def findEPI(self, prime_implicant_chart): # Функция для поиска существенных простых импликантов из диаграммы простых импликантов
        res = []
        for minterm in prime_implicant_chart:
            if len(prime_implicant_chart[minterm]) == 1:
                res.append(prime_implicant_chart[minterm][0]) if prime_implicant_chart[minterm][0] not in res else None
        return res

    def findVariables(self, bin_minterm): # Функция для поиска переменных в minterm. For example, the minterm --01 has C' and D as variables
        var_list = []
        for i in range(len(bin_minterm)):
            if bin_minterm[i] == '0':
                var_list.append(chr(i+65)+"'")
            elif bin_minterm[i] == '1':
                var_list.append(chr(i+65))
        return var_list
    
    def flatten(self, x): # преобразует вложенные списки в единый плоский список.
        flattened_items = []
        for i in x:
            flattened_items.extend(x[i])
        return flattened_items

    def findminterms(self, bin_minterm): #Функция для определения того, какие минтермы объединены. For example, -011 is obtained by merging 3(0011) and 11(1011)
        gaps = bin_minterm.count('-')
        if gaps == 0:
            return [str(int(bin_minterm,2))]
        x = [bin(i)[2:].zfill(gaps) for i in range(pow(2,gaps))]
        temp = []
        for i in range(pow(2,gaps)):
            temp2,ind = bin_minterm[:],-1
            for j in x[0]:
                if ind != -1:
                    ind = ind+temp2[ind+1:].find('-')+1
                else:
                    ind = temp2[ind+1:].find('-')
                temp2 = temp2[:ind]+j+temp2[ind+1:]
            temp.append(str(int(temp2,2)))
            x.pop(0)
        return temp

    def compare(self, a, b): # Функция для проверки, отличаются ли 2 минтермы только на 1 бит
        c = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                mismatch_index = i
                c += 1
                if c>1:
                    return (False,None)
        return (True,mismatch_index)

    def removeTerms(self, _chart, terms): #Удаляет из графика минтермы, которые уже покрыты
        for i in terms:
            for j in self.findminterms(i):
                try:
                    del _chart[j]
                except KeyError:
                    pass

    def table(self):
        output = ""
        minterms = self.minterms
        size = self.size
        groups = self.groups
        all_pi = self.all_pi
        chart = self.chart

        # Group minterms by number of 1s in binary representation
        for minterm in minterms:
            group_no = bin(minterm).count('1')
            if group_no not in groups:
                groups[group_no] = []
            groups[group_no].append(bin(minterm)[2:].zfill(size))

        # Display initial groups
        output += "Group No.       Minterms        Binary of Minterms\n"
        output += "=" * 50 + "\n"
        for group_no, group in sorted(groups.items()):
            output += f"{group_no:<15}:\n"
            for term in group:
                output += f"{'':<10}{int(term, 2):<15}{term}\n"
            output += "-" * 50 + "\n"

        # Iteratively combine groups to find prime implicants
        while True:
            tmp = groups.copy()
            groups, m, marked, should_stop = {}, 0, set(), True
            group_keys = sorted(tmp.keys())
            for i in range(len(group_keys) - 1):
                for term1 in tmp[group_keys[i]]:
                    for term2 in tmp[group_keys[i + 1]]:
                        res = self.compare(term1, term2)
                        if res[0]:
                            new_term = term1[:res[1]] + '-' + term1[res[1] + 1:]
                            if new_term not in groups.get(m, []):
                                groups.setdefault(m, []).append(new_term)
                            should_stop = False
                            marked.add(term1)
                            marked.add(term2)
                m += 1
            unmarked = set(self.flatten(tmp)).difference(marked)
            all_pi = all_pi.union(unmarked)

            if should_stop:
                break

        # Create the prime implicant chart
        for pi in all_pi:
            for minterm in self.findminterms(pi):
                if minterm in chart:
                    chart[minterm].append(pi)
                else:
                    chart[minterm] = [pi]

        # Display Prime Implicant Chart
        output += "\nPrime Implicants Chart:\n"
        output += "Minterms    | " + " ".join(map(str, minterms)) + "\n"
        output += "=" * 50 + "\n"
        for pi in all_pi:
            covered = ['X' if str(m) in self.findminterms(pi) else ' ' for m in minterms]
            output += f"{','.join(self.findminterms(pi)):<12}| {' '.join(covered)}\n"

        # Find essential prime implicants
        EPI = self.findEPI(chart)
        output += "\nEssential Prime Implicants: " + ', '.join(str(i) for i in EPI)
        self.removeTerms(chart, EPI)

        # Generate the solution
        final_result = [self.findVariables(i) for i in EPI]
        output += '\n\nSolution: F = ' + ' + '.join(''.join(i) for i in final_result)
        return output
    
def print_truth_table(variables: list[str], columns: list[str | Callable], columns_names: list[str]):
    table_columns = []

    if type(columns) != list:
        raise ValueError('Invalid type for columns')

    if len(columns_names) != len(columns):
        raise ValueError('The length of columns and column names must match')

    for column in columns:
        if isinstance(column, str):
            columns_functions = {
                'and': lambda a, b: a and b,
                'or': lambda a, b: a or b,
                'not': lambda a: not a,
            }

            if column not in columns_functions.keys():
                raise ValueError('Invalid string in columns. Must be "and", "or", or "not"')

            table_columns.append(columns_functions[column])
        elif isinstance(column, Callable):
            table_columns.append(column)
        else:
            raise ValueError('Invalid type in columns. Must be "and", "or", "not", or a function')

    header = '\t'.join(variables + columns_names)
    output = [header]
    truth_table = list(product([0, 1], repeat=len(variables)))

    for values in truth_table:
        row_values = "\t".join(str(value) for value in values)
        for column in table_columns:
            # Dynamically unpack arguments for lambda functions
            row_values += '\t' + str(column(*values[:column.__code__.co_argcount]))
        output.append(row_values)

    return '\n'.join(output)


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = QuineMcCluskeyGUI(root)
#     root.mainloop()
