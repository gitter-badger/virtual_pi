from GreyMatter import general_conversations

def brain(name, speech_test):
    def check_message(check):
        
        if speech_test == check:
            return True
        
        else:
            return False
        
    if check_message('who are you'):
        general_conversations.who_are_you()
            
    else:
        general_conversations.undefined()

