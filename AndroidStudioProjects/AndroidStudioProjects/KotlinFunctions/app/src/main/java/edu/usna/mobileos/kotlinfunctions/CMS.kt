package edu.usna.mobileos.kotlinfunctions

import java.util.Calendar

fun main(args:Array<String>){
    val myList = listOf("cat","dog","fish","canary")
    println(myList.filter{println("hmm...thinking..${it[0] == 'c'}");it[0] == 'c'})

}

fun printHello(s:String,n:Long=10.toLong()){
    println("Hello $s")
    println(n)
}

fun dayofWeek(){
    val curDay:Int = Calendar.getInstance().get(Calendar.DAY_OF_WEEK)
    val days:Array<String> = arrayOf("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
    println("What day is it today? ${days[curDay-1]}!")
}

fun whatShouldIDoToday(mood:String,weather:String="sunny",homeworks:Int=0) : String{
    when(mood){
        "sad"       ->  when(weather){
                            "sunny" -> return "go for a walk"
                            "cloudy"-> return "read a book"
                            "rainy" -> return "make hot chocolate (or better yet coffee!)"
        }
        "happy"     ->  when(weather){
                            "sunny" -> return "go get boba with a friend :)"
                            "cloudy"-> return "go for a run"
                            "rainy" -> return "put on some nice music and do a puzzle"
        }
        "motivated" ->  return "GO FOR A RUN AND DO PUSHUPS AAAARRRGGHHH"
        else -> return "ehh idk"
    }
    return "ehh idk"
}

fun isItTooHot(temp:Int) = temp > 87



