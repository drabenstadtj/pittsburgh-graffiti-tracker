from db.models import db, GraffitiEntry

# Create a new graffiti entry
def add_graffiti_entry(title, description, latitude, longitude, image_url, created_by):
    """
    Adds a new graffiti entry to the database.
    :param title: Title of the graffiti
    :param description: Description of the graffiti
    :param latitude: Latitude coordinate
    :param longitude: Longitude coordinate
    :param image_url: Path or URL of the graffiti image
    :param created_by: User who created the entry
    :return: Success or failure response
    """
    try:
        new_entry = GraffitiEntry(
            title=title,
            description=description,
            latitude=latitude,
            longitude=longitude,
            image_url=image_url,
            created_by=created_by
        )
        db.session.add(new_entry)
        db.session.commit()
        return {"success": True, "message": "Graffiti entry added successfully!", "entry_id": new_entry.id}
    except Exception as e:
        db.session.rollback()
        return {"success": False, "message": str(e)}

# Fetch all graffiti entries
def get_all_graffiti_entries():
    """
    Fetch all graffiti entries from the database.
    :return: List of graffiti entries
    """
    try:
        entries = GraffitiEntry.query.all()
        return [
            {
                "id": entry.id,
                "title": entry.title,
                "description": entry.description,
                "latitude": entry.latitude,
                "longitude": entry.longitude,
                "image_url": entry.image_url,
                "created_at": entry.created_at,
                "created_by": entry.created_by
            } 
            for entry in entries
        ]
    except Exception as e:
        return {"success": False, "message": str(e)}

# Fetch a single graffiti entry by ID
def get_graffiti_entry_by_id(entry_id):
    """
    Fetch a single graffiti entry by its ID.
    :param entry_id: Graffiti entry ID
    :return: Graffiti entry or error message
    """
    try:
        entry = GraffitiEntry.query.get(entry_id)
        if entry:
            return {
                "id": entry.id,
                "title": entry.title,
                "description": entry.description,
                "latitude": entry.latitude,
                "longitude": entry.longitude,
                "image_url": entry.image_url,
                "created_at": entry.created_at,
                "created_by": entry.created_by
            }
        return {"success": False, "message": "Entry not found."}
    except Exception as e:
        return {"success": False, "message": str(e)}

# Update an existing graffiti entry
def update_graffiti_entry(entry_id, title=None, description=None, latitude=None, longitude=None, image_url=None):
    """
    Updates an existing graffiti entry.
    :param entry_id: ID of the graffiti entry to update
    :param title: New title
    :param description: New description
    :param latitude: New latitude
    :param longitude: New longitude
    :param image_url: New image path or URL
    :return: Success or failure response
    """
    try:
        entry = GraffitiEntry.query.get(entry_id)
        if not entry:
            return {"success": False, "message": "Entry not found."}

        # Update fields
        if title: entry.title = title
        if description: entry.description = description
        if latitude: entry.latitude = latitude
        if longitude: entry.longitude = longitude
        if image_url: entry.image_url = image_url

        db.session.commit()
        return {"success": True, "message": "Entry updated successfully!"}
    except Exception as e:
        db.session.rollback()
        return {"success": False, "message": str(e)}

# Delete a graffiti entry
def delete_graffiti_entry(entry_id):
    """
    Deletes a graffiti entry from the database.
    :param entry_id: ID of the graffiti entry to delete
    :return: Success or failure response
    """
    try:
        entry = GraffitiEntry.query.get(entry_id)
        if not entry:
            return {"success": False, "message": "Entry not found."}
        
        db.session.delete(entry)
        db.session.commit()
        return {"success": True, "message": "Entry deleted successfully!"}
    except Exception as e:
        db.session.rollback()
        return {"success": False, "message": str(e)}

# Search graffiti entries by title
def search_graffiti_by_title(keyword):
    """
    Searches graffiti entries where the title matches a given keyword.
    :param keyword: Keyword to search for in graffiti titles
    :return: List of matching graffiti entries
    """
    try:
        entries = GraffitiEntry.query.filter(GraffitiEntry.title.ilike(f"%{keyword}%")).all()
        return [
            {
                "id": entry.id,
                "title": entry.title,
                "description": entry.description,
                "latitude": entry.latitude,
                "longitude": entry.longitude,
                "image_url": entry.image_url,
                "created_at": entry.created_at,
                "created_by": entry.created_by
            } 
            for entry in entries
        ]
    except Exception as e:
        return {"success": False, "message": str(e)}
