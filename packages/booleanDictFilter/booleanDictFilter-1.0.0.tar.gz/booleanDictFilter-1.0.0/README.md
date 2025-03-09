# BooleanDictFilter
Sometimes it is necessary to be able to make a filter which is a string, that evaluates the contents of a dictionary object.  Sure we could write that in Python and use eval, but that would be considered a security risk.   Instead we use a conditional boolean string, which can handle the comparisons we need.

## Operands
|Operand| Description | example
|--|--|--
| and | logical and | (condition) and (condition)
| or | logical or | (condition) or (condition)
| not | logical not | not (condition)
| >= | key is greater then or equal to value | _key_ >= integer
| <= | key is less then or equal to value | _key_ <= integer
| > | key is greater then value | _key_ > integer
| < | key less then value | _key_ <= integer
| == | key equals value | _key_ == integer , _key_ == string
| contains | key contains string | _key_ contains string
| anyof | any of the defined keys are in dict | anyof(_key_, [_keyname1_, _keyname2_])
| noneof | none of the defined keys are in dict | noneof(_key_, [_keyname1_, _keyname2_])
     
## Features
Other then typical boolean operations and evaluations.  I added the following evaluators to the flow, to make things a bit simpler. 

 - **contains** if the value of _key_ is a string, and contains the string specified, this returns true.  If _key_ is not a string this returns false. 
 - **anyof** if the value of _key_ is any of one the values specified in the list, then this returns true. Useful to remove a bunch of OR statements.
 - **noneof** if the value of _key_ is not in the list of values specified, then this returns true.  

If any of the _key_ does not exist in the dictionary, then result is false.  However this is dependent on the _key_ being reached.  For instance:

    (name == "John") or (nonexistentkey == "X")

 Would be true, if the key "name" was "John" in the given dictionary.

## Installation

To install, run:

```bash
pip install booleanDictFilter
```
## Examples
Allows for testing a single, or group of dictionaries against a text defined filter.   

    import BooleanDictFilter from BooleanDictFilter 
    filter_str = "(anyof(role, ['admin', 'moderator']) and age >= 30)"  
    bf = BooleanDictFilter(filter_str)
    print (bf.evaluate({"role": "admin", "age": 35, "status": "active", "name": "John"})) # True
    print (bf.evaluate({"role": "user", "age":34, "status": "active", "name": "June"})) # False

The same filter can be used to evaluate a list of dictionaries, returning only those dictionaries which passed the evaluation:

    import BooleanDictFilter from BooleanDictFilter
    filter_str = "(anyof(role, ['admin', 'moderator']) and age >= 30)"  
    bf = BooleanDictFilter(filter_str)
    data_list = [  
    	{"role": "admin", "age": 35, "status": "active", "name": "John"},
    	{"role": "user", "age":34, "status": "active", "name": "June"}
    ]
    filtered_data = bf.filter_dicts(data_list)  
    for item in filtered_data:  
        print(item)
Result:

    [  
    	{"role": "admin", "age": 35, "status": "active", "name": "John"}
    ]

## License

This project is licensed under the MIT License.


