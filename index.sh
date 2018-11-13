workdir=`pwd`; echo "Current working dir : $workdir";
sourcedir="${workdir}/computer_chapters/"; echo "Source dir is : $sourcedir";
touch ${workdir}/include_computer_chapters_tex.tex
include_chapters_tex=${workdir}/include_computer_chapters_tex.tex
echo $include_chapters_tex
echo "% This tex file is generated by get_computer_chapters/index.sh automatically." >> $include_chapters_tex
for chapter_tex in `ls -F $sourcedir `; do
    # echo ${chapter_tex/_/-} # 把下划线替换成-
    _chapter_tex=${chapter_tex/_/-}
    # echo ${_chapter_tex%%.*} 
    echo "\subsection{"${_chapter_tex%%.*}"}">> $include_chapters_tex
    echo "\input{computer_chapters/"$chapter_tex"}" >> $include_chapters_tex
done;

# % \subsection{001哲学基本问题及其内容（对哲学的划分）}
# % \input{001_哲学基本问题及其内容（对哲学的划分）/sum}