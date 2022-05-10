## Guión segunda entrega

In the last update we set the bases of our project and let our imagination fly, but now we had to consider the time and the resources we had to make it possible.

First of all we had to make a lot of changes to the requirements, the first of which was regarding the time interval of our collected data . We had planned to store the information in a database and to be able to archive it and retrieve it later, but problem is, we do not know enough about databases to make it work and we would spend a considerable amount of time setting one up, so we changed the time period of our data from: “The last 1,6 and 12 months” to:  “the last month.”

After some minor tweaks to our requirement, we started working on the mockups, which we did not really develop in the first update of our project. First we started with the design of the program logo, that is pretty beautiful, we are not going to lie, our design stands out anywhere. 

Next we move on to the program interface, the way that we show the users all the information. In the beginning we did not dedicate enough time to the wireframes and didn’t have a base to guide us, we had designed a menu that did not have a requirement where it would list the characteristics that it will have. Our buttons were not detailed on their position, or content either. We worked on our solution, the interface design standard, where we have all the specifications in relation to the graphs, the buttons, filters and colors, so that the interfaces look similar and don’t lose the essence of the program. All these mockups and specifications can be checked on our online repository in github.

Next, we defined the keywords that we would use to scrape the technologies requested on these job postings. These keywords are designed to be able to collect the most precise information from the page and this have a lower volume of unnecessary information. Now that we have where to look for the info and we established the structure of the data we will be working on. 

At the beginning of the project we defined a coding standard to follow, now we tried to find a tool to do this automatically and we did it, but to make use of this tool we had to make some changes to our standard, we followed a manual that you can find on our github repository. 

On the standard we define things like the variables, functions, classes and files naming, where in the most of those we use lowercases, except on the classes where we use capwords; we also use underscores to replace spaces. 

The way to do comments and the code design is also included on the standard and there is where the tool makes its appearance, because it checks the indentation(indetenshen) (4 spaces) and add or remove the spaces that it needs to follow the standard.

After that, we started to put together our pieces of code. To scrape Glassdoor’s data  we use ChromeDriver, a webdriver for chrome, and run a script using python and Selenium. The code works by opening a Google chrome tab and searching in the glassdoor page for software engineer jobs in Mexico, and then locates the information through the sites’ DOM and stores it in a Dataframe. We had to overcome certain challenges, such as: a window pop up that would come up after clicking a job offer that we had to close in order to keep scraping data; having to click the “show more” button in order to have full access to the data; and cleaning the collected Data, which was a lot to go through.

We logged all these activities on the github’s activity log, a new tool that professor Cambranes recommended to us in a weekly meeting. In that log we created all the activities and were assigned to a team member with a little description and a deadline. We had extra meetings to check all the progress we made, as well as followed the same method of measuring participation that we used for the first update, split the assignments in a way that would allow everyone to have a relevant participation in the project; all these documents can be consulted in our github repository.

This is the second update of our project, thank you.
