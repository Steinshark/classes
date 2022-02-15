package edu.usna.mobileos.presidentslist

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class TextItemViewHolder (view : View) : RecyclerView.ViewHolder(view) {
    val textView: TextView = view.findViewById(R.id.itemTextView)

    fun bind(presidentName: String, listener: PresidentListener) {
        textView.text = presidentName
        textView.setOnClickListener { listener.onItemClick(presidentName) }
    }

}



class PresidentsAdapter(val data: Array<String>, val listener: PresidentListener) :
    RecyclerView.Adapter<TextItemViewHolder>() {

    override fun getItemCount() = data.size

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): TextItemViewHolder {
        val layoutInflater = LayoutInflater.from(parent.context)
        val view = layoutInflater.inflate(R.layout.item_layout, parent, false)

        return TextItemViewHolder(view)
    }

    override fun onBindViewHolder(holder: TextItemViewHolder, position: Int) {
        holder.bind(data[position],listener)

    }
}



interface PresidentListener {
    fun onItemClick(president: String)
}
