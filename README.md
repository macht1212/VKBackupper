![VKBackuper](img/VKBackuper.jpg)
By Alexander Nazimov

## Programm Description

There are situations when you don’t want to make backups of photos on your own that were uploaded as the main ones for the page in VK, or the sources have long been lost, but you still want to save them, then you can use the backup directly to your Yandex disk.
 
## API Used

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.



## Authors

- [@macht1212](https://github.com/macht1212)
- Netology School

