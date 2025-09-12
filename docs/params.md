# Parameters

GribCheck expects each entry in the parameter list to include four sections:

- **name**: A unique name for the parameter.  
- **pairs**: A list of key/value pairs used to match the parameter in the GRIB file.  
- **expected**: A list of key/value pairs expected to be present in the GRIB file.  
- **checks**: A list of checks to run on the parameter.  

```json
[
  {
      "name": "name",
      "pairs": [
          {"key": "k1", "value": "v1"},
          {"key": "k2", "value": "v2"}
      ],
      "expected": [
          {"key": "k3", "value": "v3"},
          {"key": "k3", "value": "v4"},
      ],
      "checks": [
          "c1",
          "c2"
    ]
  }
]
```
Creating these files can be tedious because you often encounter repetitive patterns that are simply copy-pasted.  
This approach is error-prone and hard to maintain.  
The example below demonstrates this problem.  

```json
{
  "name" : "specific_snow_water_content_ml",
  "expected" : [
    {"key": "values", "min": [-100000000.0, 100000000.0], "max": [-100000000.0, 100000000.0]}
  ],
  "pairs" : [
    {"key": "paramId", "value": 76},
    {"key": "discipline", "value": 0},
    {"key": "parameterCategory", "value": 1},
    {"key": "parameterNumber", "value": 86},
    {"key": "typeOfFirstFixedSurface", "value": 105},
    {"key": "scaleFactorOfFirstFixedSurface", "value": 0}
  ],
  "checks" : [
    "point_in_time",
    "given_level"
  ]
},
{
  "name" : "specific_snow_water_content_pl",
  "expected" : [
    {"key": "values", "min": [-100000000.0, 100000000.0], "max": [-100000000.0, 100000000.0]}
  ],
  "pairs" : [
    {"key": "paramId", "value": 76},
    {"key": "discipline", "value": 0},
    {"key": "parameterCategory", "value": 1},
    {"key": "parameterNumber", "value": 86},
    {"key": "typeOfFirstFixedSurface", "value": 100}
  ],
  "checks" : [
    "point_in_time",
    "given_level",
    "pressure_level"
  ]
},
{
  "name" : "specific_snow_water_content_hl",
  "expected" : [
    {"key": "values", "min": [-100000000.0, 100000000.0], "max": [-100000000.0, 100000000.0]}
  ],
  "pairs" : [
    {"key": "paramId", "value": 76},
    {"key": "discipline", "value": 0},
    {"key": "parameterCategory", "value": 1},
    {"key": "parameterNumber", "value": 86},
    {"key": "typeOfFirstFixedSurface", "value": 103},
    {"key": "scaleFactorOfFirstFixedSurface", "value": 0}
  ],
  "checks" : [
    "point_in_time",
    "given_level",
    "height_level"
  ]
}
]
```

A closer look shows that the three entries are very similar or even identical in many places.  
We can identify three patterns that cause code duplication:

- The **name** sections only differ by a suffix (`_ml`, `_pl`, or `_hl`), while the base name is the same for all three parameter variants of `specific_snow_water_content`.  
- The **expected** sections are identical in all three parameter variants.  
- In the **pairs** section, the first four entries are the same, and in the **checks** section, the first two entries are the same.  

In the next section, we’ll demonstrate how to use Jsonnet to describe such parameters more generically, eliminating code duplication and adding restrictions to catch errors early.  


## Jsonnet

Jsonnet is a data templating language that extends JSON.  
Its main purpose is to use a programming language to generate JSON files.  
With Jsonnet, you can use variables, functions, conditionals, imports, and other programming constructs to create JSON data that follows the structure required by GribCheck.

Jsonnet also comes with a command-line tool that converts Jsonnet files into JSON files.  
The examples in this document can be run and tested using this Jsonnet tool. 

```bash
jsonnet example.jsonnet
```

### Importing files

One useful feature of Jsonnet is the ability to **import files**.  
This allows you to store parameters in separate files, organize them in a clear structure, and reuse them easily.

The example below illustrates this idea:  
Assume we have two lists, each stored in a separate file, and we want to combine them into a single list.  
To achieve this, we import `ext.jsonnet` into `main.jsonnet` and use the `+` operator to concatenate the imported list with the new list.  


ext.jsonnet
```json
[
  {name : "hl"}
]
```

main.jsonnet
```json
local ext = import 'ext.jsonnet';

[
  {name : "ml"},
  {name : "pl"},
] + ext
```

When we run the example, we should get the following output.

```bash
#!/bin/bash
jsonnet main.jsonnet
```

```
[
   {
      "name": "ml"
   },
   {
      "name": "pl"
   },
   {
      "name": "hl"
   }
]
```

### Generic parameters

The previous example showed how to import files and concatenate lists.  
Now, we’ll demonstrate how to use Jsonnet to describe parameters in a more generic way, avoiding code duplication and adding restrictions to catch errors early.  
We’ll use the **TIGGE** example from above to illustrate this idea.

As mentioned earlier, many entries in the sections are similar or repeated.  
Jsonnet provides features that allow us to describe these three entries in a generic way, reduce duplication, and enforce validation.

First, in `templates.jsonnet`, we define a base class that represents a **parameter skeleton**.  
This skeleton includes the four sections expected by GribCheck and is configured to throw an error if the `name` field is missing.  
This ensures that any derived classes follow the proper structure and always include a valid name.  

templates.libsonnet
```json
{
Parameter: {
    name: error "Please set a parameter name",
    pairs: [],
    checks: [],
    expected: [],
  },
}

```

Next, we create a new file called `inheritance.jsonnet` and import the template using the `import` keyword.  
The imported data is assigned to a variable named `templates`.  

We then define a new **parameterized class** that takes a `type` as an argument.  
This `type` is used to specify the **name** by appending it as a suffix to the base name.

In the **pairs** section, we first define the key/value pairs used to match the three parameters.  
We then use the `+` operator to extend the list based on a condition:  
- If the condition is true, we add a list with one entry.  
- If the condition is false, we add an empty list.  

This ensures the list is extended dynamically based on the passed `type`.  

A similar approach is applied to the **checks** section, allowing us to extend it conditionally as well.  

The **expected** section is the same for all three parameter variants.  
We simply define the expected values once, and they will appear identically in all variants.  

At the end of the file, we define a list containing three instances of the `ParamId76` class.  
The only difference between them is the argument passed to each instance.  
The final parameters are generated from this list.


inheritance.jsonnet
```json
local templates = import 'templates.libsonnet';

local ParamId76(type) = templates.Parameter + {
  name: "specific_snow_water_content" + "_" + type,
  pairs: [
    {key: "paramId", value: 76},
    {key: "discipline", value: 0},
    {key: "parameterCategory", value: 1},
    {key: "parameterNumber", value: 86},
  ]
  + (if type == "ml" then [{key: "typeOfLevel", value: 105}] else [])
  + (if type == "ml" then [{key: "scaleFactorOfFirstFixedSurface", value: 0}] else [])
  + (if type == "pl" then [{key: "typeOfLevel", value: 100}] else [])
  + (if type == "hl" then [{key: "typeOfFirstFixedSurface", value: 103}] else [])
  + (if type == "hl" then [{key: "scaleFactorOfFirstFixedSurface", value: 0}] else []),
  expected+: [
    {key: "values", min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0]}
  ],
  checks: [
    "point_in_time",
    "given_level",
  ] 
  + (if type == "pl" then ["pressure_level"] else [])
  + (if type == "hl" then ["height_level"] else []),
};

[
ParamId76("ml"),
ParamId76("pl"),
ParamId76("hl"),
]
```

