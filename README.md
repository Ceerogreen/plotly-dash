# plotly-dash
Connor Rose DS4003
Website: https://plotly-dash-34lb.onrender.com

The purpose of this app is to display historic March Madness data. This can be used for people who care about specific teams, and want visualizations of how their team historically does, and by users looking forward to compare the stats of current teams to the performance of similar teams in the past. This is something I do consistently, and while some sites like KenPom are helpful, they are not exceptionally functional or interactive like this application is.

The dashboard building process was an incredible amount of trial and error, as all good projects are. The first page I made was the most complicated one, being the Yearly Statistics page. I found a layout design for that page that worked really well, and made it highly functional, then used that as a model to build the other pages off of. I mainly focused my work on functionality, adding CSS styling at the very end. I wanted to include as many easily laid out interactable items as possible - I focused on having grids for my graphs, and keeping all interactable items (sliders, radios, dropdowns, etc.) in a line, vertically or horizontally.

This project has taken a lot of resilience and scouring documentation, as well as forums. To make my graphs with logos was a long process starting with an hour of finding and properly naming files with logos for every single possible team. Afterwards, I scoured forums to find a method to turn the graph markers into logos; after finding out this is not an option for plotly markers, I attempted to use a matplotlib graph, but the method to use matplotlib graphs was depreciated. After many hours, I found a single StackOverflow post explaining how to plot an image on a graph at a specific coordinate, and was able to use this to ultimately plot the logos found on the yearly statistics page's graphs, and I could then turn the marker opacity to 0. At any point I could've given up on this, but decided it was important and worthwhile, and managed to stick it out. Ultimately, I've come up with a project I'm proud of, that I think has excellent ease of use, any lack of which is made up for in strong page descriptions. I was perseverant, and focused on a simplistic yet human design, which is a hallmark of what I do.
