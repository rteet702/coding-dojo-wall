# m_flask_template
<p>This is a modularized flask template, ready to go.</p>
<p>Template credit and thanks to: rteet702</p>


## BASHRC
<p>This template is used with bashrc code to clone the template into a new project directory. 
  To get the full benefit of this template, add the following code snippets to your bashrc file:</p>
  
  ```bash
  function pyi(){
      pipenv install flask PyMySQL flask-bcrypt && echo "-------------------FLASK PYMYSQL BCRYPT AND VIRTUAL ENVIRONMENT CREATED-------------------"
  }
  export -f pyi
  
  function gitmflasktemplate(name){
    git clone https://github.com/code-Brian/m_flask_template.git && echo "------------------- GIT REPO CLONED -------------------"
    mv m-flask-template $1
    cd $1 && echo "------------------- CHANGING INTO PROJECT DIRECTORY -------------------"
    rm -rf .git && echo "------------------- GIT FILE DELETED -------------------"
    pyi && echo "------------------- INSTALLING FLASK AND PYMYSQL -------------------"
  } 
  export -f gitmflasktemplate
  ```
In order to generate the template using this method, after updating your .bashrc file, run the command:
```bash
gitmflasktemplate some-project-name
```

## Git

This project also works perfectly fine just by cloning the git repository. 
A few notes:
- This repository is intended to be a template, so everything is a placeholder. 
- In order to create your own repository for the project you are working on, you will likely need to delete .git inside the cloned repository.


## Lastly
<p> I hope this template is helpful. Please ping myself or Robert (https://github.com/rteet702) if there are any questions!</p>