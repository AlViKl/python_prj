from app.utils.gen_functions import show_basic_functions
from app.utils.gc_plot import generate_plot_with_data
from app.db_management.data_init import fill_tables
from app.db_management.data_configuration import db_drop, db_create


def main():
    db_drop()
    db_create()
    fill_tables()
    show_basic_functions()
    generate_plot_with_data()


if __name__ == "__main__":
    main()
