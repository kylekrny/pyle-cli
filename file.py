from config import get_config

def generate_jsx_code(config, file_name):
    import_statement = "import React from 'react';" if not config["import"] else ""

    component_string = ""

    if config["component"] == "arrow":
        component_string = f"""
        const {file_name} = () => {{
            return (
                <div>
                    {file_name}
                </div>
            );
        }};"""
    elif config["component"] == "functional":
        component_string = f"""
        function {file_name}() {{
            return (
                <div>
                    {file_name}
                </div>
            );
        }};"""
    else:
        component_string = f"""
        class {file_name} extends React.Component {{
            render() {{
                return (
                    <div>
                        {file_name}
                    </div>
                );
            }}
        }};"""
    
    component_code = f"""
    {import_statement}

    {component_string}

    export default {file_name};
    """

    return component_code


def create_file(directory, fileName):
    config = get_config()
    file_string= f"src/{directory}/{fileName}.{config['language']}"
    try:
        with open(file_string, "x") as file:
            file.write(generate_jsx_code(fileName))
    except:
        print (f"{fileName} already exists in {directory} directory")