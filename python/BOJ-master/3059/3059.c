main(t,i,r,s){int e[26];scanf("%d\n",&t);while(t--){for (i=0;i<26;i++)e[i]=0;r=0;for(;(s=getchar())!=10;){if(!e[s-65]){r+=s;e[s-65]=1;}}printf("%d\n",2015-r);}}