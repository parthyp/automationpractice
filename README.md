# automationpractice

# due to time restrain i could not optomize code as well as create it how i would.


firsttest.py

this would be test i would create if we need to get things on a go where the scripts are not optomize

there are several things i could have work with such as get cypress to do this.

but i was not sure wheather this would need mobile cases as well.

I do have some lines of code which shoes how to find things and fill things but i felt it was too repeatitive so i did not finish it all the way

because we get the idea for most part


ideal_test.py

this is where i get exicted. i wish i had time but due to week away from cyber 5 at current job and personal holiday i didnt have time i wanted.

I want to make this as page object model with our own apis to do things.

page object model:

 Pages folder: each things as its own class..
    ex. - sign up page: class for each of the fields as well as each verifications with some logs

    Action Folder: there would be our own apis to do different action from selenim/appium/assertions. so if things do changes, it would be easy to update

 Data Folder: if a page requires data, it must store in data folder. it must always get data from there. no hardcoding

 Component: this would hold every action on that page. so signUpComponent file would have signUpUser() checkError() checkSuccuesMsg() ect.

 Test folder:

   Every Test would have launch_browser function that would launch browser on their needs.

   We would take appropiate functions from component to test things.

   tear down functions which cleans up things


As far as ci/cd goes:

it is set up but i cant run things as i dont have selenium grid server set up. so test would fail.

Here are my example ci/cd where i kick off pipelines as soon as new commit comes in. its not test dedicated but it uses simple YAML to do things 
