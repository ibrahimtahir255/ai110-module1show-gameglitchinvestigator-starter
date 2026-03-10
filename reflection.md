# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?  
The game lagged a little and took some time to get started. For example, I could not see the prompt box to enter my guess and it appeared after a few seconds the page loaded.  
The first time I ran it, I could see the first answer did not get added to the history list in the debug info. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards"). 
  1) The hint logic is broken because even though the secret number is higher it always says go lower. I would expect the hints to be correct. 
  2) The start game logic does not work. Once you run out of tries you cannot restart the game. I would expect the game to restart and reset everything. 
  3) Pressing the new game button only refreshes the secret and not the score and history. I would expect the score to be reset and the history and also the attempts
  4) Attempts is initialized with 1 when instead it should be 0. 
  5) Max score we get is 70 not 100. 
  6) The secret value is just any number between 1-100 without regard to the acceptable range of that level

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?  
Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).  
AI suggested that the check_guess implementation is wrong in that the hint directions are swapped. I verified this by running the app and indeed they were wrong.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).  
Did not come across an example of an AI suggestion that was incorrect. Howver, I notcied that most of the times AI made the decisions for me if I did not give it enough context for example whats the max score that can be achieved if you answer correctly on the first try. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?  
I wrote pytest for each of the bugs, checked if they passed, and then also ran the app to see if they were actually fixed in real life
- Describe at least one test you ran (manual or using pytest) 
  and what it showed you about your code.  
Since the code had a glitch where the hints were wrong/swapped, I fixed it and then for example wrote a test case: test_too_high_hint_message(). This tested the check_guess() function to see if it correctly returned the correct hint. In this case, for example, if the guess was higher than the secret then the function should return the hint "LOWER"
- Did AI help you design or understand any tests? How?
Yes! I designed all my tets using AI and then there were some tests it generated that I did not understand. I told it to help me understand those particular test cases and it explained them to me. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.  
The secret number doesnt change, the stored value stays the same but the type of the secret changes on evry other guess. On even attempts, 42 == "42" is Flase in Python because an integer and a string are never equal. So even if you type the exact right number, the game says you're wrong every other attempt.   

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Reruns work in a way that every time you click a button on a webpage, the entire page refreshes from scratch. Every click runs all your Python code again from line 1 to the last line.  
Session state is like a small notepad that Streamlit keeps on the side. Even when the page reruns, anything you wrote on that notepad survives. So instead of storing your score in a regular variable, you store it in st.session_state.score.  

- What change did you make that finally gave the game a stable secret number?
The fix is to just use: secret = st.session_state.secret. 
This means check_guess always compares two integers, so the correct guess is always recognized regardless of which attempt number you're on.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? 
  - This could be a testing habit, a prompting strategy, or a way you used Git.  
  I really like creating test cases and I want to take this along as I work through future projects. This just helps you verfiy your bug fixes and make sure the application is robust.   
- What is one thing you would do differently next time you work with AI on a coding task?  
I would do more work trying to play with the application yself and have an understanding of what I need to fix instead of letting AI do it for me. It would just allow me to be more in control and feel a sense of ownership over my work and product. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.  
I realized that AI is really helpful and it can be used to assist in coding, planning, and deubugging but its not okay to blindly let AI take control and do whatever it says.
