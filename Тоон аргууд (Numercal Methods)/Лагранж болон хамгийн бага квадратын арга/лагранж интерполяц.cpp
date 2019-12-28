
/*
Лагранжийн интерполяц гүйцэтгэж буй c++ кодыг нэмж оруулав.

*/




#include <fstream>
#include <stdio.h>
#include <vector>
#include <cassert>
#include <iostream>

using namespace std;

// Basis functions
double lk(double x0, vector<double>& x, int k)
{
    double res = 1.0;
    
    for (int i = 0; i < x.size(); i++)
        if (i != k) res *= (x0 - x[i]) / (x[k] - x[i]);
    
    return res;
}

//Lagrange Function
double lagrange(double x0, vector<double>& x, vector<double>& y)
{
    assert(x.size() == y.size());

    double res = 0;
    for (int k = 0; k < x.size(); k++)
        res += y[k] * lk(x0, x, k);
    return res;
}

int main(){

	//int x[10]={};
	//int y[10]={};
	vector<double> a(10);
	vector<double> b(10);
	double ans;

	ofstream myfile;
	ofstream myfil;
  	myfile.open ("example.txt");
  	myfil.open ("k_lk.txt");
  	


	for(int i=0; i<10;i++){
		a[i]=i;
		b[i]=0.5*a[i]-1;
		myfile << a[i]<<" "<<b[i]<<'\n';
	}

	myfile.close();

	int k=-1;
	for(int j=0; j<=10; j++){
		myfil << k<<" "<<lk(k,a,9)<<" "<<lagrange(k,a,b)<<'\n';
		k++;
	}

	myfil.close();
	
	//int s=0;
	//int z=sizeof(x)/sizeof(x[0]);
	//int r=sizeof(y)/sizeof(y[0]);

	//ans=lagrange(1,a,b);
	//double answer=lk(1,a,7);
	//printf("%i\n",ans);
  	//cout<<ans<<endl;

  	return 0;

}
