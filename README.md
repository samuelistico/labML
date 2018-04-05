# LABML

## DECISION TREE

Current working version is in python_src, to run it you just need python > 3 and run python main.py this will train a new tree using the data in data.csv and then validate and print the accuracy using training_data.py

it works by getting the attribute with the best info gain using the entropy formula and then recursively calculating sub trees for each case of that best attribute. The tree is therefore built bottom up as a python dictionary (key,value data structure)

For the predictions we travers these dictionary using the proposed best path until we hit a leaf node

the data sets have to be used as they are saved in the folder

* main.py contains driver and validation code 
* dTree.py contains the creation of the tree
* data_manager.py contains code to manage, clean and provide data
* dTreeUtils.py contains extra functions used

Example of generated tree in python
```javascript
{
  'BP-STBL': {
    'mod-stable': {
      'L-BP': {
        'mid': {
          'L-SURF': {
            'mid': 'S',
            'high': 'A'
          }
        },
        'high': 'A',
        'low': 'A'
      }
    },
    'unstable': {
      'L-O2': {
        'good': {
          'SURF-STBL': {
            'unstable': {
              'L-CORE': {
                'mid': 'S',
                'low': 'A'
              }
            },
            'stable': 'I'
          }
        },
        'excellent': 'A'
      }
    },
    'stable': {
      'COMFORT': {
        '10': {
          'L-SURF': {
            'mid': {
              'L-CORE': {
                'mid': {
                  'SURF-STBL': {
                    'unstable': 'A',
                    'stable': 'A'
                  }
                },
                'low': 'S'
              }
            },
            'high': 'A',
            'low': 'A'
          }
        },
        '15': 'S',
        '07': 'S'
      }
    }
  }
}
```

