import codecs
import io
import sys
import textfsm
import terminaltables


AMOUNT_REMAINING = int(sys.argv[1])
TEMPLATE_FILE_NAME = "./templates/wide_data.template"
DATA_FILE_NAME = "./data/wide_data.txt"


def get_text_from_file(file_name):
    with codecs.open(file_name, "r", "utf-8") as input_file:
        return input_file.read()        


def sort_pole(elem):
    return elem[2]


def main():
    data_to_be_parsed = get_text_from_file(DATA_FILE_NAME)
    template_text = get_text_from_file(TEMPLATE_FILE_NAME)
    
    template_io = io.StringIO(template_text)
    template_io.seek(0)
    
    parser = textfsm.TextFSM(template_io)
    parsing_result = parser.ParseText(data_to_be_parsed)
    parsing_result.sort(key=sort_pole)
    print("parsing_result:\n{}".format(parsing_result[:AMOUNT_REMAINING:]))

    # table_to_be_printed = terminaltables.AsciiTable(
    #     [parser.header] +
    #     parsing_result
    # )
    
    # print("Parsed Data:\n{}".format(table_to_be_printed.table))
    # for item in parsing_result:
    #     print(item)
    #     print("*************")

main()




