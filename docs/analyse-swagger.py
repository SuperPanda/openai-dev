import yaml
import json

def parse_swagger_file(swagger_file_path):
    with open(swagger_file_path, 'r') as file:
        swagger_data = yaml.safe_load(file)

    major_components = {}
    actions = {}
    models = {}

    # Extracting major components from tags
    if 'tags' in swagger_data:
        for tag in swagger_data['tags']:
            name = tag.get('name', 'UnnamedComponent')
            description = tag.get('description', 'No description provided.')
            major_components[name] = {
                "description": description,
                "actions": []
            }

    # Extracting actions (the morphisms) from paths
    for path, methods in swagger_data.get('paths', {}).items():
        for method, operation in methods.items():
            tags = operation.get('tags', [])
            if tags:
                component_name = tags[0]  # Assuming the first tag is the component name
                if component_name in major_components:
                    action_name = operation.get('operationId', f"{method.upper()} {path}")
                    major_components[component_name]["actions"].append(action_name)
                    actions[action_name] = {
                        "method": method.upper(),
                        "path": path,
                        "summary": operation.get('summary', 'No summary provided.'),
                        # Include additional details as necessary
                    }

    # Extracting models and their fields
    '''
    for model_name, schema in swagger_data.get('components', {}).get('schemas', {}).items():
        model_description = schema.get('description', 'No description provided.')
        model_fields = schema.get('properties', {})
        
        models[model_name] = {
            "description": model_description,
            "fields": []
        }
        
        for field_name, field_attributes in model_fields.items():
            models[model_name]["fields"].append({
                "name": field_name,
                "type": field_attributes.get('type', 'undefined'),
                "description": field_attributes.get('description', 'No description provided.'),
                # Include additional details as necessary, such as `required`, `enum`, `format`, etc.
            })
    '''
    return major_components, actions #, models

def main():
    # Specify the path to your Swagger file
    swagger_file_path = 'swagger.openapi.yaml'

    # Parse the Swagger file
    #major_components, actions, models = parse_swagger_file(swagger_file_path)
    major_components, actions = parse_swagger_file(swagger_file_path)

    # Print the results (or use them as needed in code generation)
    print("Major Components:")
    print(json.dumps(major_components, indent=2))
    print("\nActions:")
    print(json.dumps(actions, indent=2))
    #print("\nModels:")
    #print(json.dumps(models, indent=2))

if __name__ == "__main__":
    main()
