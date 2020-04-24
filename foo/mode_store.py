import AllInformation
import AllCommands
import list_output
import data

def ModeStore(bookname,book):
    list_output.output_list(book,bookname)
    print(AllInformation.mode_store_done)
    return