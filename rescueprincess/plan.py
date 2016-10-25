#!/usr/bin/python3

"""
Michael duPont
Proposed Solution to:
https://assets.toggl.com/images/toggl-how-to-save-the-princess-in-8-programming-languages.jpg
"""

class Plan:
    @staticmethod
    def execute():
        print('You saved the princess without having to write any code!')
    @staticmethod
    def party():
        raise Exception('Partied too hard with all that extra time you had')

if __name__ == '__main__':
    try:
        Plan.execute()
        Plan.party()
    except Exception as e:
        print('Error:', e)
