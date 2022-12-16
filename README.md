![VKBackuper](img/VKBackuper.jpg)  
By Alexander Nazimov

## Programm Description

There are situations when you don’t want to make backups of photos on your own that were uploaded as the main ones for the page in VK, or the sources have long been lost, but you still want to save them, then you can use the backup directly to your Yandex disk.
 
## Implemented methods 

### VK Class:
#### Get information about user by user_id and his personal token
```python
get_info
```
Method returns information about User in JSON format.  
Response includes First name, Last Name, age, sex, and other information about profile.  

## **Attention!**

Token is **personal information!**  
Please do not shear it!

| Method     | Params         | Description                               |
|:-----------|:---------------|:------------------------------------------|
| `get_info` | `access_token` | asked for personal token                  |
|            | `user_id`      | asked for user_id                         |
|            | `v`            | API version. <br/>Curent version is 5.131 |

#### Get information about user by user_id and his personal token
```python
get_photo_info
```
Method returns data in JSON format. Includes photo's URL, size type and name of image.
Name of image generated as count of likes. If counts are same, date in UNIX added to likes.

| Method            | Params             | Description                                                                               |
|:------------------|:-------------------|:------------------------------------------------------------------------------------------|
| `get_photo_info`  | `access_token`     | asked for personal token                                                                  |
|                   | `owner_id`         | asked for user_id                                                                         |
|                   | `v`                | API version. <br/>Curent version is 5.131                                                 |
|                   | `count`            | number of last photos from profile                                                        |
|                   | `extended`         | 1 - added additional information (likes, comments, etc. <br/> 0 - no (standart)           |
|                   | `album_id`         | profile - photos from profile folder<br/>wall - photos from wall<br/>saved - saved folder |


#### Saving data in JSON format
```python
save_info
```


| Method        | Params    | Description                                                    |
|:--------------|:----------|:---------------------------------------------------------------|
| `save_info`   | no params | method takes data from previous method and <br/> saved to JSON |


### Yandex.Disc Class

#### Get headers
```python
get_headers
```

Method returns headers for access to account.

```python
return {'Content-Type': "application/json", 'Authorization': f'OAuth {self.token}'}
```

#### Get upload link from Yandex API
```python
get_upload_link
```


| Method            | Params       | Description         |
|:------------------|:-------------|:--------------------|
| `get_upload_link` | `path`       | asked path to file  |

#### Create a new folder in Ya.Disc
```python
new_folder
```
| Method            | Params      | Description         |
|:------------------|:------------|:--------------------|
| `get_upload_link` | `path`      | asked path to file  |
|                   | `overwrite` |                     |

#### Using VK Class to get links for upload
```python
get_photos_links_from_vk
```

| Method        | Params    | Description                        |
|:--------------|:----------|:-----------------------------------|
| `save_info`   | no params | method takes data from VK method   |


#### Upload to Ya.Disc

```python
upload
```
| Method    | Params      | Description           |
|:----------|:------------|:----------------------|
| `upload`  | `path`      | asked path on Ya.Disc |
|           | `url`       | asked URL of photo    |
|           | `overwrite` |                       |


## Authors

- [@macht1212](https://github.com/macht1212)
- Netology School

