import collections
import zipfile


# You can delete the war-and-peace.txt file and it wil unpack the zip file.
def unzip(archive):
    z_file = zipfile.ZipFile(archive, 'r')
    for i_name in z_file.namelist():
        z_file.extract(i_name)
    z_file.close()


def collect_stats(file_name):
    if file.endswith('.zip'):
        unzip(file_name)
        file_name = ''.join((file_name[:-3], 'txt'))
    result = dict()
    text_file = open(file_name, 'r', encoding='UTF-8')
    for i_line in text_file:
        for j_char in i_line:
            if j_char.isalpha():
                if j_char not in result:
                    result[j_char] = 0
                result[j_char] += 1

    text_file.close()
    return result


def sort_by_freq(stats_dict):
    sorted_values = sorted(stats_dict.values())
    sorted_dict = collections.OrderedDict()
    for i_value in sorted_values:
        for j_key in stats_dict.keys():
            if stats_dict[j_key] == i_value:
                sorted_dict[j_key] = stats_dict[j_key]

    return sorted_dict


def print_stats(stats):
    print("+{:-^19}+".format('+'))
    print("|{: ^9}|{: ^9}|".format('letter', 'frequency'))
    print("+{:-^19}+".format('+'))
    for char, count in stats.items():
        print("|{: ^9}|{: ^9}|".format(char, count))
    print("+{:-^19}+".format('+'))


file = 'war-and-peace.zip'
stats = collect_stats(file)
stats = sort_by_freq(stats)
print_stats(stats)
