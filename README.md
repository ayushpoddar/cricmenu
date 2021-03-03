# CricMenu
Live cricket score on MacOS Menu Bar

[Download here](https://github.com/ayushpoddar/cricmenu/blob/main/CricMenu.zip)

## Instructions:

1. Download the [ZIP file](https://github.com/ayushpoddar/cricmenu/blob/main/CricMenu.zip)
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