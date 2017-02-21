# Problem:
#
# Sample Input:
# 4 2
# 0 1
# 2 3
#
# Sample Output:
# 4
#
# Explanation:
#
# Persons numbered 0 and 1 belong to same country, and those numbered 2 and 3 belong to same country. So the UN can choose one person out of 0 & 1 and another person out of 2 & 3. So the number of ways of choosing a pair of astronauts is 4.

# Solution

N, P = input().strip().split(' ')
pairs = []
for i in range(int(P)):
    pairs.append(list(map(int,input().strip().split(' '))))

def append_missing_astros(list_of_country_with_astros):
    for i in range(int(N)):
        astro_found = False
        for country_with_astros in list_of_country_with_astros:
            if i in country_with_astros:
                astro_found = True
                break
        if not astro_found:
            list_of_country_with_astros.append(set([i]))
    return list_of_country_with_astros

def split_astronauts_by_country(pair_list):
    list_of_country_with_astros = [set(pair_list[0])]
    for pair in pairs:
        country_found = False
        astros_in_found_country = {}
        remove_merged = False
        for country_with_astros in list_of_country_with_astros:
            if (pair[0] in country_with_astros) or (pair[1] in country_with_astros) :
                if country_found:
                    country_with_astros.update(astros_in_found_country)
                    remove_merged = True
                    break
                country_with_astros.update(pair)
                astros_in_found_country = country_with_astros
                country_found = True
        if not country_found:
            list_of_country_with_astros.append(set(pair))
        if remove_merged:
            list_of_country_with_astros.remove(astros_in_found_country)
    return append_missing_astros(list_of_country_with_astros)

def calculate_no_of_possible_pairs(list_of_country_with_astros):
    no_of_pairs = 0
    for count in range(len(list_of_country_with_astros)):
        for i in range(count+1,len(list_of_country_with_astros)):
            no_of_pairs += len(list_of_country_with_astros[count]) * len(list_of_country_with_astros[i])
    return no_of_pairs

print(calculate_no_of_possible_pairs(split_astronauts_by_country(pairs)))