import praw


previous_id="0"
		
reddit = praw.Reddit(    
        user_agent="by u/Sam-Kinison-Bot",
        client_id="hoT0dxAKni29GjA9XEJOmA",
        client_secret="xnAqn5RemYcstRoKA4zBpTUNMmibzQ",
        username="Sam-Kinison-Bot",
        password="WeRGr00t",)

previous_id="0"
	
def search():
	for results in reddit.subreddit('all').comments():	#Grab all the Recent Comments in every subreddit. This will return 100 of the newest comments on Reddit
		global previous_id	#Import the global variable
		
		body = results.body  #Grab the Comment
		body=body.lower()	#Convert the comment to lowercase so we can search it no matter how it was written
		comment_id = results.id  #Get the Comment ID
		
		if comment_id == previous_id:  #Check if we already replied to this comment
			return "Error"
		

		
		found=body.find('. it is a joke.')	#Search for Sad. Make sure there is a period at the end of the previous sentence as well as the end of SAD
			
		if found != -1: 		#Looks like the comment includes . sad.
			previous_id = comment_id  #Add to our global variable
			
			try:
				results.reply('CAUSE IT IS A FUCKING JOKE OHHH OHHH OHHHHHHHHHHHHH')	#Reply to the Comment
			except:
				break	#Leave the function if error occurs with replying
		

