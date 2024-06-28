import sys


def main():
    if len(sys.argv) > 1:

        if sys.argv[1].lower() == "cli":
            import cli_version as output_module
        elif sys.argv[1].lower() == "gui":
            import gui_version as output_module
        else:
            import cli_version as output_module
    else:
        import cli_version as output_module


    output_module.main()

if __name__ == '__main__':
    main()
