package edu.usna.mobileos.h3_stenbergeverett

/*

fun main(){
    val fish = MandarinFish("henry",8)
    println("name: ${fish.name}, size: ${fish.size}, color: ${fish.color} ")
}

// Fish is the base class
abstract class Fish(var name : String,var size : Int = 10) {
    init{println("fish name: ${name}, fish size: ${size}")}
    public fun get(){println(name)}
    abstract fun careForFish()
}

// This is-a Fish, and it implements the FishColor interface
class MandarinFish(name: String, size : Int,  color : FishColor = BlueFishColor ) :  Fish(name,size), FishColor by BlueFishColor{
    override fun careForFish() {
        println("to care for ${name}, please do: \n1) Clean the tank often\n2) Feed once a day\n3) Read a bedtime story at least once a week ")
    }
}

// Represents the fish's color
interface FishColor{
    val color : String
}

// Represents the fish color 'blue'
object BlueFishColor : FishColor{
    override val color : String = "blue"
}
 */
fun main(){
    val fish = MandarinFish("henry",8)
    println("name: ${fish.name}, size: ${fish.size}, color: ${fish.color} ")
}

// Fish is the base class
abstract class Fish(var name : String,var size : Int = 10) : FishColor by BlueFishColor {
    init{println("fish name: ${name}, fish size: ${size}")}
    public fun get(){println(name)}
    abstract fun careForFish()
}

// This is-a Fish, and does NOT have to implement FishColor because the 'Fish' color has already done that
class MandarinFish(name: String, size : Int,  color : FishColor = BlueFishColor ) :  Fish(name,size) {
    override fun careForFish() {
        println("to care for ${name}, please do: \n1) Clean the tank often\n2) Feed once a day\n3) Read a bedtime story at least once a week ")
    }
}

// Represents the fish's color
interface FishColor{
    val color : String
}

// Represents the fish color 'blue'
object BlueFishColor : FishColor{
    override val color : String = "blue"
}
