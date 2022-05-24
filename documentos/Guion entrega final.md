## Guion para el vídeo sobre la entrega final

Hello people, we are space team and we are going to show you the whole process that we had to go through to be able to carry out our project, we hope you enjoy it, let's go for it.

The process of our project began with the approach of the problem, are we really informed about the demand for Software engineers in the field? Do we know what companies are looking for today? This project is aimed at future Software Engineers, focusing on third-year students with the purpose of enabling them to pursue a full time job or position that they feel interested in, by giving them an advantage when looking for a permanent position through information of the market.

The solution we came up with to face this issue was to collect the necessary data, through the web scraping technique, of the Glassdoor website. Despite the fact that this information is available, we noticed that the site only does not archive past offers and is missing key filters that are necessary when job hunting and getting to know the market in general, so we decided to focus on these two important points to work on our project.

The functionalities we proposed were based on having a variety of filters, both general and specific, where the user can obtain a graphic display of the data that they have requested.


Once we set the bases of our project, as a next step we focused on writing its requirements. To do this, we used a table to organize them from highest to lowest priority in order to have a plan and be able to differentiate which should be mandatory, high priority, preferred but not necessary and which would remain as proposals.

For our first installment, we decided to focus on the system being able to collect the data to be stored in a database; a bar graph that would use the requested filters of the information and that saves these graphs to present them to the user.

The filters that we proposed at the beginning were divided into general and specific. The general filter would include: salary information, time interval, location in Mexico, company size and whether the job was remote or on-site. For the specific filters, they would be classified by location (the 32 states of the Republic), company size (large, medium and small), position type (on-site, virtual or hybrid).

Once we were clear about the data that the system would include, we began with the design of the interface that our project would have. As a first step, we designed our wireframes, adding how the charts would be displayed and where the buttons for the filters would be. Having this idea, we proceeded to the development of our wireframes, mockups and logo, in order to have a more detailed interface and have an idea of what the final product of the project would look like. In the mockups we added the visualization of the graphs, which we decided would be represented as bar graphs and the buttons would be dropdowns for the filters. The previous can be consulted on our project’s public repository.

A very important point that we considered was the name of our project, we decided to name it LinkJob.
As we progressed in our project, for the second installment we made a modification of the requirements. One of them was regarding the time interval, we had established that it would be “the last 1, 6 and 12 months”, but not being very familiar with databases, we decided to change it to a considerable amount of “1 month". Another point that we had to change, a little later, was in the part of the filters, the location would no longer be in the specific filters since when we were graphing we noticed that the graph doesn’t match and it wouldn’t make sense, we also had to change the specification of "the 32 states of the Republic" because in some job offers they don’t mention the state, but the city, so change it to states would be very complicated and a little unnecessary for us. As a last modification, we realized that the hybrid modality wasn’t within the job offers, so we had to discard it.

Before we started coding, we established a coding standard, we found a tool to do it automatically so we had to modify some things in our standard following the manual upload in our github repository.

As the first pieces of code made in the second installment, we begin with collecting the information from the Glassdoor platform using the Chrome webdriver for which we create a code that when executed, using Python and the Selenium method, automates the navigation and collection of the site’s information. Once we have our collected data, we store it in a dataframe, with the csv format to have it in table form and reach a better organization of it.

For the debugging of our data, we use the Pandas library. Once we scrapped the information, we had a lot of unnecessary data so we decided to filter each category of information, leaving only the data that is needed to make the graphs. One of these cases would be in the company size part, since in our dataframe they appeared within a range, so we had to apply slight glimpses of functional programming such as the lambda function to apply some actions to all the rows in a dataframe.
With the debugging, we noticed that we would need another debugging for the bid count because it varies depending on the filters that are required. We decided to create several functions that are based on creating a new dataframe where the general filter and the specific filter appear, which would indicate the amount that this filter is repeated in the general filter.

Having this data, we begin to encode the graphs. To do this, we use the matplotlib library to create and customize them according to the interface that we propose in the mockups. We graph the different cases that would be obtained by selecting the general and specific filter buttons with functions so that the graphs follow a format according to the axes, quantities, data, title and color. Having the resulting graphs, in the end we established them as .png format to be able to use them in the interface.

For the graphical interface we use Tkinter, a module that is already included with Python to customize our project, adding drop-down buttons for the different filters of the information categories, as well as the graph that would be generated when selecting a specific one, the palette of colors and the LinkJob logo.

The organization of the team during the development of the project was essential to be able to achieve the proposed objectives, to reach this, we made an activity log, which helped us to distribute the tasks to be carried out each week, in this case we used Github, in which we organize the tasks in: Activity to Perform, Activity in Process, Activity to Review and Activity Finished.

In order to review the progress, we had, at least, two meetings per week. On Saturdays we met through discord to distribute the tasks, review the progress of the project and see it future projection. Also, when we need to review a specific issue between us, we notify through our WhatsApp group and schedule a meeting as soon as possible. On Wednesdays we met through Microsoft Teams with Dr. Edgar Cambranes to evaluate the previous progress and provide feedback. 

On the other hand, the distribution of the activities to be carried out by each member of the team was also a fundamental role for the achievement of the project, since we divided the tasks thinking in our abilities, and thus we managed to be more efficient, exploiting the potential of each member of the team, always trying to be as equitable as possible.

And in the end, in order to evaluate the participation of each member, we made a contribution table, where we noted the activities carried out by each member, to which a score was assigned depending on the importance and difficulty of the same, to thus, add the points for each member and obtain their qualification during the first, second and third presentation.

With this we conclude the third and last update of our project, so we will proceed to show a demonstration of our program.
