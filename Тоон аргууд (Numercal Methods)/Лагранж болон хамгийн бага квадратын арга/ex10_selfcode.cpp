#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <assert.h>
#include <string.h>

using namespace std;

int evaluations = 0;
int maxDepth    = 0;

// Our function expression
double f (double t) { return exp(-3 * t) * sin (4*t); }

void integration_trapezoidal_rule(double &lower, double &upper,int &n,double &result){

	int N=n-1;
	double h;

	h=(upper-lower)/N;
	result=0;
	
	for(int i=0; i<N; ++i){
		result=result+h*(f((lower+i*h))+f((lower+(i+1)*h)))/2;
	}	
}

double recursive(double &low, double &up,double &sf,double epsilon, int depth = 1){
	
	double m;
	int const_n=11;
	double ans_l;
	double ans_r;
	double an;

	m=(low+up)/2;

	//Adaptive_trapezoidal_rule(low, up,const_n,ans);
	Integration_trapezoidal_rule(low, m,const_n,ans_l);
	Integration_trapezoidal_rule(m, up,const_n,ans_r);

	an=ans_l+ans_r;

	 // use Richardson extrapolation to estimate the error
	 double error = (an - sf);
	  

	  // if accuracy is reached, return the result obtained by Richardson extrapolation  epsilon/2,
	  if ( fabs (error) <= epsilon || depth == 100 ) {
	    evaluations += 1;
	    if (depth > maxDepth)
	      maxDepth = depth;
	    return an;
	  }


return recursive(low,m,ans_l,epsilon/2,depth+1)+recursive(m,up,ans_r,epsilon/2,depth+1);
 
}


int main(int argc, char const *argv[])
{
	
	//Given data values
	double l=0;
	double r=4;
	double eps=pow(10,-6);
	double res;
	int num=11;
	double answer;

	Integration_trapezoidal_rule(l, r,num,res);
	answer=recursive(l,r,res,eps);
	cout<<res<<' '<<answer<<endl;

	// RESULT WILL BE:  0.108659 0.160001
	
}