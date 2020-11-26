using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
	public float speed = 5f;
	private Rigidbody2D rb;

    // Start is called before the first frame update
    void Start()
    {
		rb = GetComponent <Rigidbody2D>();
    }

    // Update is called once per frame
    void Update()
    {
        float moveX = Input.GetAxis ("Horizontal");
				rb.MovePosition (rb.position + Vector2.right * moveX * speed * Time.deltaTime);
				if (Input.GetKeyDown (KeyCode.Space))
					rb.AddForce (Vector2.up * 4500);
    }
}
