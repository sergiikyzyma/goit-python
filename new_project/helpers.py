import random

INTENTS = ["exit", "help", "hello", "show"]
ACTIONS = ["clean", "addcontact",  "addnotes", "changecontact", "changenotes", "deletecontact", "deletenotes", "findcontact", "findbytag", "name", "phone", "birthday", "address", "peaple"]
TAGS = ["raider", "elergy", "special"]
    
BOT_HANDLERS = {
    'intents': {
        'exit': {
            'examples':['bye', 'exit', 'thank you', "that`s all"],
            'responses':['Bye', 'Have a nice day', 'It was pleasure to help you']
        },
        'hello': {
            'examples':['hi', 'hello'],
            'responses':['Hi. How could I help you?', 'Hello. What do you want, guy?', 'Good day. I ready to help you']
        },
        'help': {
            'examples':['help', 'need help', 'help me'],
            'responses':["""
                        My name is Addy and I am your AddressBook assistant.
                        I was created to help you fill out your address book.
                        The address book consists of the
                        contact's name, phone numbers, and the contact's birthday, for now.
                        Together, we can expand it.
                        Below you will find all the commands that I can perform for you:
                        1. show all - I'll show you the whole addressbook and all information about all users
                        2. name, phone, birthday, email or address {value} - I'll show you the {value} contacts from the addressbook
                        about one or more users by a few digits of the phone number or letters of the name
                        3. add contact John 481-234-56-78 - I'll add the new contact {name} and {phone, birthday, email or address} to you addressbook
                        4. remove contact John 481-234-56-78 - I'll remove the phone from the contact
                        5. remove contact John 04-04-1978 - I'll remove the birthday from the contact
                        6. change contact John 481-234-56-78 481-234-56-79 - I'll change the first phone of the contact on new one
                        7. change contact John 04-04-1978 04-04-1979 - I'll change the first birthday of the contact on new one
                        8. find phone John - I'll show you phone and in how many days the contact's birthday will be.
                        9. find birthday John - I'll show you in how many days the contact's birthday will be.
                        10. find email John - I'll show you email and in how many days the contact's birthday will be.
                        11. find address John - I'll show you address and in how many days the contact's birthday will be.
                        12. find all John - I'll search through the contents of the contact book. I will show you all the information about one user
                        13. find notes John - I'll show you notes about user and in how many days the contact's birthday will be.
                        14. find by tag <tag> - I'll show you notes about all users by tag and in how many days the contact's birthday will be.
                        15. peaple {number} - search peaple, who birth for {number} days
                        16. addnotes {name} {tag} {note} - adding note by tag
                        17. changenotes {name} {tag} {old_note} (new_note) - changing note by tag
                        18. deletenotes {name} {tag} {note} - changing note by tag
                        """]
        },
        'show': {
            'examples':['show all', 'could you show all the contacts', 'please, show all the contacts', 'showall'],
            'responses':['OK', 'Look here', 'Sure', 'You got it']
        },
    },
    'actions':{
        'clean': {
            'examples':['clean me this folder', 'clean'],
            'responses':['Sure', 'I can find it', 'Of course']
        },
        'addcontact': {
            'examples':['add contact','add phone','add birthday','add email','add address', 'addcontact', 'could you add the value', 'please, add the one value'],
            'responses':['OK', 'No problem', 'I got it']
        },
        'addnotes': {
            'examples':['addnotes','add notes', 'addnote', 'add notes'],
            'responses':['OK', 'No problem', 'I got it']
        },
        'changecontact': {
            'examples':['changecontact', 'change contact', 'could you change phone'],
            'responses':['Yes, Sir', 'I can do it', 'Never give up']
        },
        'changenotes': {
            'examples':['changenotes', 'change notes'],
            'responses':['Yes, Sir', 'I can do it', 'Never give up']
        },
        'deletecontact': {
            'examples':['removecontact', 'remove contact', 'deletecontact', 'delete contact'],
            'responses':['OK', 'No problem', 'I got it']
        },
        'deletenotes': {
            'examples':['deletenotes', 'delete notes'],
            'responses':['OK', 'No problem', 'I got it']
        },
        'findcontact': {
            'examples':['findcontact', 'find contact'],
            'responses':['Sure', 'I can find it', 'Of course']
        },
        'findbytag': {
            'examples':['findbytag', 'find by tag'],
            'responses':['OK', 'Look here', 'Sure', 'You got it']
        },
        'name': {
            'examples':['name', 'show me contacts', 'could you show me some contacts', 'please, show me contacts'],
            'responses':['OK', 'Look here', 'Sure', 'You got it']
        },
        'phone': {
            'examples':['phone', 'show me phone', 'could you show me some phone', 'please, show me phone'],
            'responses':['OK', 'Look here', 'Sure', 'You got it']
        },
        'birthday': {
            'examples':['birthday', 'show me birthday', 'could you show me some birthday', 'please, show me birthday'],
            'responses':['OK', 'Look here', 'Sure', 'You got it']
        },
        'email': {
            'examples':['email', 'show me email', 'could you show me some email', 'please, show me email'],
            'responses':['OK', 'Look here', 'Sure', 'You got it']
        },
        'address': {
            'examples':['address', 'show me address', 'could you show me some address', 'please, show me address'],
            'responses':['OK', 'Look here', 'Sure', 'You got it']
        },
        'peaple': {
            'examples':['peaple', 'give me peaple', 'give me peaple of birthday'],
            'responses':['OK', 'Look here', 'Sure', 'You got it']
        },
    },
    'failure_phrases': [
        "Could you repeat, please?",
        "I did not understand you",
        "Please, repeat one more time",
        "Could you rephrase, please?",
        "Иди погуляй с такими запросами",
        "Выспись",
        ]
    }
