package com.gulogulo.starterapp;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import org.json.JSONObject;

public class info extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_info);
        try{
            JSONObject obj = new JSONObject(getIntent().getStringExtra("response"));
            String text = obj.getString("link");
            TextView t = (TextView) findViewById(R.id.link);
            t.setText(text);
            Log.d("yes", text);
        }
        catch (org.json.JSONException j){
            Log.d("jsonerror", j.toString());
        }
    }
}
