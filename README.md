### Your Task
For our introduction, we want to get familiar with creating a new Django application. Create a new application that serves recipes from different authors, much like our demo application does for news. Intended layout:

An index page that lists all titles of the loaded recipes (they don't have to be real recipes; just fill them with lorem ipsum and some numbers.)
Each title is a link that takes you to a single page with the content of that recipe.
Each detail view for a recipe has the author name, along with all the information for the recipe arranged in a reasonable format.
Clicking on the author's name should take you to an Author Detail page, where you can see a list of all the recipes that the Author has contributed to.
Make editing all of the models accessible through the admin panel only.
So we have three types of pages: a simple list view, a recipe detail view, and an author detail view. The admin panel will handle the creation views, so we don't need to worry about that.