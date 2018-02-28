void solveHanoi(int N,int S, int I,int T){
	if (N >1){ 
		solveHanoi(N-1,S,T,I);
		cout << "Move" << N << "from peg" << S << "to" << T << endl;
		solveHanoi(N-1,I,T,S);
	}
	else if(n==1){
		cout << "Move"<<N
	}


}