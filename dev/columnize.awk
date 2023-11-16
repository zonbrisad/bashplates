BEGIN{
  w=0;
}
{
  lines[NR]=$0;
  l=length($0);
  w=l>w?l:w;
} 
END{
  wd=W>0?W:w;
  h=rshift(NR,1)+(NR%2);
  for (i=1;i<=h;i++) {
    printf "%*s %s %*s\n",-wd,lines[i],sep,-wd,lines[i+h];
  }
}
