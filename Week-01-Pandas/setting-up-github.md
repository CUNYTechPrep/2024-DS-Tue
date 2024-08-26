# setting-up-github for CTP

## VERY IMPORTANT first step, Setup! 
0. Complete the setup.md install instructions from the Summer HW Phase 1 setup instructions here:  https://github.com/CUNYTechPrep/2024-python-summer-prep/blob/main/setup.md
	* You should have already done this, however, if you did not do this yet, complete the guide above or else this will def fail. 
## Authing Github
* Follow instructions [provided here](https://github.com/CUNYTechPrep/2024-python-summer-prep/blob/main/setup-part-2-github.md) 
* Stop before the 'Making Sure It Works - Create and Edit your own Repo' section.  We will be doing that part later today. 


## Forking The Repo
0. Create a fork of this repo. ![forking](https://raw.githubusercontent.com/zd123/images-for-class/main/forking-image-instructions/01-fork-button.png)

0. Name that fork `my-fork-2024-fall-data-science` ![enter image description here](https://github.com/zd123/images-for-class/blob/main/forking-image-instructions/02-naming-fork.png?raw=true)
	
0. Copy the link of your forked repo.  ![enter image description here](https://github.com/zd123/images-for-class/blob/main/forking-image-instructions/03-getting-fork-link.png?raw=true)

0. Open your terminal

0. Clone your forked version of the original version by typing in `git clone` then pasting the link you just copied. 
	* `git clone https://github.com/[YOUR-GITHUB-USER-NAME]/my-fork-2024-fall-data-science.git`

## Setting it up to listen for updates. 

0. Navigate to inside that repo. 
	* `cd my-fork-2024-fall-data-science`

0. Set the upstream (Note this is the link of the CUNY Tech Preps version of the repo, not your fork)
	* IF YOU ARE IN __TUESDAYS__ CLASS:  
		* `git remote add upstream https://github.com/CUNYTechPrep/2024-DS-Tue`
	* IF YOU ARE IN __WED__ CLASS: 
		* `git remote add upstream https://github.com/CUNYTechPrep/2024-DS-Wed`
	* IF YOU ARE IN __FRI 1230__ CLASS: 
		* `git remote add upstream https://github.com/CUNYTechPrep/2024-DS-Fri-1230`
	* IF YOU ARE IN __FRI 630__ CLASS: 
		* `git remote add upstream https://github.com/CUNYTechPrep/2024-DS-Fri-630`

## Doing, Uploading/Pushing, and Submitting your HW

0. Make a copy of `Exercise-DONT-EDIT-MAKE-COPY.ipynb`
0. Name the new copy as `Exercise-[YOUR-INITIALS].ipynb`. Zack DeSario's would be `Exercise-ZD.ipynb`.


#### Doing your HW. 
0. Highly suggest spening your repo directory folder/file in VS Code.  You can easily run ipython notebooks in there, and even have git intergration. 


0. If you are not using VS Code then... Open your termial, type into your terminal and run
	* `jupyter notebook`
	* If that doesn't work, run `jupyter lab`

0. This should have launched a web page.  In that page, navigate to Week-01/Exercise-[YOUR-INITIALS].ipynb notebook.

0. In the first cell print your name
	* `print('[SOMETHING NICE ABOUT YOUR TA]')`

0. Save the file by clicking the disk icon in the top right or `Command+s`. Or clicking the floppy-disk icon in the top right. 


## Uploading/Pushing Your HW
*Adding your changes and pushing them to github so they are viewable the internet*

0. In your terminal that is in repo where you just edited the Exercise file....
0. Add your changes 
	* `git add Week-01-Pandas/Exercise-[YOUR-INITIALS].ipynb`
0. Commit your changes
	* `git commit -m '[YOUR COMMIT MESSAGE HERE]'`
0. Push your changes
	* `git push`

## Sanity check
0. Go to YOUR FORKED github repo. 
0. Navigate to Week-01 and click on the Exercise-[YOUR-INITIALS].ipynb file.
0. YOU SHOULD SEE YOUR `print('[SOMETHING NICE ABOUT YOUR TA]')` edits.
0. Make sure you can see the changes you made. 
0. Copy that exact URL, it should look something like this. https://github.com/zd123/my-fork-2023-fall-data-science-fridays/blob/main/Week-01-Pandas/Exercise-ZD.ipynb 
0. Paste that URL next to your name in the HW Submission Sheet. 
	* [ZD TO CREATE Tuesday's HW Submission Sheet](https://docs.google.com/spreadsheets/d/1HJb_Hf0dVCOWhw-jimE-E9bnFCROZ1Hx_GLRlQhQ8lA/edit#gid=0)
	* ZD CREATE WED. 
	* [ZD TO CREATE  Friday's 12:30 HW Submission Sheet](https://docs.google.com/spreadsheets/d/1JjyMHmS0n8IuCcYihp5Z9YtTDwsE2ygwIPUqT0tEowE/edit#gid=0)
	* [ZD TO CREATE Friday's 3:30 HW Submission Sheet](https://docs.google.com/spreadsheets/d/1PbQ1JI9cC9WZUnJoEgfoFWhXw7a5wx-53p7bmQmKhKI/edit#gid=0)


## If youre having auth issues... 
* See step 0.  
* First try to update git: https://git-scm.com/downloads 
* [Follow Guide This Setup Guide](https://github.com/CUNYTechPrep/2024-python-summer-prep/blob/main/setup-part-2-github.md)


If you're still having issues... Follow these instructions CAREFULLY.
* https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

* https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
