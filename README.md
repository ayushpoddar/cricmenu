# CricMenu
Live cricket score on MacOS Menu Bar

[Download here](https://github.com/ayushpoddar/cricmenu/releases/download/1.0.0/CricMenu.zip)

## How does it look
![England vs India 4th Test - Ahmedabad - 2021](https://i.imgur.com/9gzLLsE.png)

## Instructions:

1. Download the [ZIP file](https://github.com/ayushpoddar/cricmenu/releases/download/1.0.0/CricMenu.zip)
2. The ZIP file contains the application
3. Copy the URL of the match from [ESPNCricInfo](https://www.espncricinfo.com/)
4. Paste the URL in the dialog box that pops up when the application is opened
5. Allow notifications if you want notifications for boundaries and wickets
6. Enjoy!

P.S: You get the option to enter another match's URL from the options in the app.

## Support
I have tested the app on my Macbook Air (MacOS Big Sur).

Would love to hear about your feature requests and issues you face. Send me an email at [ayush.mail.id@gmail.com](mailto:ayush.mail.id@gmail.com)

## Todo

1. Show the user a list of ongoing matches and allow her to choose from them.
2. Show live scorecard summary in the menu pop up.
3. Integrate live commentary with significant events like boundaries and wickets.
4. Redirect the user to relevant page upon clicking on the notification.
5. If the user has access to a streaming platform, save clips of significant events.

## Known issues

1. Currently, the score API is fetched every 10 seconds in a new thread. This causes two issues:
  - After the score is updated, the second thread resets it to the older score.
  - Double notifications for a single event.

## Installation help

When opening the app for the first time, MacOS will warn you that this app is from an unverified developer. Do the following after the warning pop up comes:
1. In the pop up shown, do NOT click on **Move to Bin**. Just click on the **Cancel** button.
2. Go to **System preferences**
3. Go to **Security & Privacy**
4. In the **General** tab, you will find an **Open Anyway** button. Click on that.
   ![Open unverified developer's app](https://i.imgur.com/vDzsaEv.png)
5. Click on **Open** in the confirmation pop up that Mac shows you next
