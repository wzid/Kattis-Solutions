from sys import stdin
from collections import defaultdict

def custom_sort(pairs):
  """
  Sorts a list of pairs by integer first, then string alphabetically in case of ties.

  Args:
      pairs: A list of tuples, where each tuple contains an integer and a string.

  Returns:
      A new list of sorted pairs.
  """

  def sort_key(pair):
    # Access the integer and string elements of the pair
    integer, string = pair
    return (integer, string.lower())  # Sort strings alphabetically, case-insensitive

  return sorted(pairs, key=sort_key)

project_to_people = {}
people_to_project = defaultdict(str)
dont_use = set()

in_project = ''
for line in stdin:
    line = line.strip()
    if line == '0':
        break
    elif line == '1':
        results = []
        for project, people in project_to_people.items():
            results.append((project, people))
        results.sort(key=lambda x: (-len(x[1]), x[0]))
        for project, people in results:
            print(project, len(people))
            # if project == 'YOUBOOK':
            #     print(*people)
        project_to_people = defaultdict(list)
        people_to_project = defaultdict(str)
        dont_use = set()
        in_project = ''
    elif line[0].isupper():
        #print(line)
        in_project = line
        project_to_people[in_project] = []
    elif in_project:
        person = line
        if person in dont_use:
            continue
        if person in people_to_project:
            if people_to_project[person] == in_project:
                continue
            dont_use.add(person)
            project = people_to_project[person]
            del people_to_project[person]
            project_to_people[project].remove(person)
        else:
            people_to_project[person] = in_project
            #print(in_project, person)
            project_to_people[in_project].append(person)
    else:
        print('Error')
        print(6/0)
        
        
    