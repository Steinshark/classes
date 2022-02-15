package edu.usna.mobileos.h2stenbergeverett

import java.util.Random

//Create a main function that:
//calls the isGoodCatName("Harley") function and prints the returned string - you will create the function later
//calls the makeNumbers() function - you will create the function later
//calls the useLambdas() function - you will create the function later

fun main(){
    println(isGoodCatName("Harley"))
    makeNumbers()
    useLambdas()
}

fun isGoodCatName(catName : String) : String{
    val return_string : String

    //assign how good/bad the name is
    when(catName.length){
        0       -> return_string = "Error: please provide a name"
        in 3..12   -> return_string = "Good cat name"
        else    -> return_string = "OK cat name"
    }

    return return_string
}

fun makeNumbers(){
    //Create the int array
    val intArr = arrayOf(11,12,13,14,15)
    var mutableStringList : MutableList<String> = MutableList(0)

    //Create the String list
    for(n in intArr){
        mutableStringList.add(n.toString())
    }

    //Print the String list
    for (s in mutableStringList){
        println(s)
    }

    //Create a list of numbers between 0 and 100 that are div by 7
    val intDivBy7 : MutableList<Int> = MutableList(0)
    for (i in 0..100){
        if(i % 7 == 0) {
            intDivBy7.add(i)
        }
    }
}

fun useLambdas(){
    val rollDice = {sides : Int -> sides == 0 0 ?: (1 + Random().nextInt()) % sides }



}