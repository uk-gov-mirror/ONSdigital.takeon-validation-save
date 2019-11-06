def parse_validation_save_data(json_input):

    outputJson=[]
    for row in json_input:
        formula_dict = {}
        formula_dict['formula'] = row['formula']
        formula_dict['triggered'] = row['triggered']
        formula_dict['validation'] = row['metadata']['validation']
        formula_dict['reference'] = row['metadata']['reference']
        formula_dict['period'] = row['metadata']['period']
        formula_dict['survey'] = row['metadata']['survey']
        formula_dict['validationid'] = row['metadata']['validationid']
        formula_dict['bpmid'] = row['metadata']['bpmid']
        formula_dict['instance'] = 0
        outputJson.append(formula_dict)
    
    validation_outputs = {}
    validation_outputs.update({'validation_outputs' : outputJson})
    print('Parsed Validation Output: ' + str(validation_outputs))
    return validation_outputs
