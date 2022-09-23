#! /bin/bash

# To automate the process of generating files in the format required by Prof. Krauss in PHYS 305.
# Pass 'tar' as an argument to tar your files.

makedir(){
	## Makes a new directory depending on the directories already
	## present. Yes, entering it as a number is both easier and more
	## robust. But I wanted to flex B)
	dirs=$(ls -d */)
	num=0
	## echo $dirs
	for i in $dirs
	do
		echo ${i::-1}
		while [[ "${i::-1}" -gt "$num" ]]
		do
			num=$((num+1))
		done
	done
	num=$((num+1))
	echo "Assignment Number $num"
	mkdir $num
}

copy_template(){
	## Copies the template into the working directory.
	## Edits the filename depending on user input and
	## the assignment number + problem number.
	## Calls edit_template on each file created.
	read -e -p "Number of Problems ": NO_PROBLEMS
	for (( i=1; i<=$((NO_PROBLEMS)); i++ ))
	do
		echo "Problem Number $i"
		read -e -p "Problem Name ": PROBLEM
		filename="${PROBLEM}_${assignment_num}_${i}.py"
		cp temp.py "${assignment_num}/$filename"
		echo "Created ${assignment_num}/$filename"
		edit_template
	done
}

edit_template(){
	## Edits the file template depending on the ass_no and 
	## problem number and description. And the filename.
	
	## soln line
	string="Solution to Problem Set ${assignment_num}, Problem ${i}."
	sed -i "s/^Solution to Problem Set*/${string}/" ${assignment_num}/$filename
	## description
	read -e -p "Problem Description ": DESCRIPTION
	sed -i "s/^<problem description>/${DESCRIPTION}/" ${assignment_num}/$filename
	## args
	sed -i "9 a\	./${filename} <args> ## REMEMBER TO ADD ARGS!" ${assignment_num}/$filename
	echo "Edited ${assignment_num}/$filename"
}

tar_files(){
	## Tars 'em up.
	## Now we take the directory
	## as user input cuz yeah lol
	read -e -p "Directory? ": DIR
	tar -czvf "avichalk_${DIR}.tgz" ${DIR}
	# tar -tzf "avichalk_${DIR}.tgz"

}

if [[ "$1"  ==  "tar" ]]
then
	tar_files
else
	makedir
	assignment_num=$num
	copy_template
fi
