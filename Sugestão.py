#### Buscar usuário pelo id

@router.get("/{id}",
            response_description="Get a single user by id", response_model=User)
async def route_get_by_id(id: str, request: Request):
    return await get_user(request.app.database.["users"].ObjectId(str(id)))

    async def get_user(user_id):
        try:
            data = await users_collection.find_one(user_id)
        if data:
            return data
    except Exception as e:
        print(f'get_user.error: {e}')


### deletar um usuário

@router.delete("/{id}", response_description="delete a user")
async def route_delete_user(id: str, requests: Request):
    return await delete_user(requests.app.database.users, ObjectId(str(id)))


## atualizar contato:

async def update_user(users, user_id, user_address):
    try:
         data = {k: v for k, v in user_database.items() if v is not None}

        user = await users_collection.update_one(
            {'_id': user_id},
            {'$set': data}
        )

        if user.modified_count:
            return True, user.modified_count

        return False, 0
          except Exception as e:
        print(f'update_user.error: {e}')
