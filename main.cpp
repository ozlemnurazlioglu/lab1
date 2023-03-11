#include <iostream>
using namespace std;

int main() {
    int var1, var2;
    cout << "Enter the value of var1: ";
    cin >> var1;
    cout << "Enter the value of var2: ";
    cin >> var2;

    int sum = var1 + var2;
    int diff = var1 - var2;
    int prod = var1 * var2;

    cout << "var1 = " << var1 << endl;
    cout << "var2 = " << var2 << endl;
    cout << "sum = " << sum << endl;
    cout << "diff = " << diff << endl;
    cout << "prod = " << prod << endl;








    std::string name;
    int studentId;


    std::cout << "Hello, what is your name? ";
    std::getline(std::cin, name);


    std::cout << "Nice to meet you, " << name << "!\n";


    std::cout << "Please enter your student id: ";
    std::cin >> studentId;


    std::cout << "Your student id is: " << studentId << "\n";


    




    std::string Name;
    float lab_grade, midterm_grade, final_grade, last_score;

    std::cout << "Enter student's name: ";
    std::getline(std::cin, name);

    std::cout << "Enter lab grade : ";
    std::cin >> lab_grade;

    std::cout << "Enter midterm grade : ";
    std::cin >> midterm_grade;

    std::cout << "Enter final grade : ";
    std::cin >> final_grade;

    last_score = lab_grade * 0.25 + midterm_grade * 0.35 + final_grade * 0.4;

    std::cout << "Student " << name << "'s final score is " << last_score << std::endl;





    cout << "*\n**\n***\n**\n*\n";


    return 0;
}