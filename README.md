## Folder Structure

```
chimney_farms/
├── api/
│   ├── main.py                  # FastAPI app entrypoint

│   ├── routes/                  # All routers
│   │   ├── __init__.py
│   │   └── customer_route.py    # Customer-related routes

│   ├── core/                    # Core utilities & settings
│   │   └── lifespan.py          # App startup/shutdown logic

│   ├── db/                      # Database-related modules
│   │   ├── __init__.py
│   │   ├── engine.py            # create_async_engine + retry logic
│   │   ├── session.py           # AsyncSession + get_session
│   │   └── init.py              # DB table creation logic

│   ├── dtos/                    # SQLAlchemy DTOs
│   │   ├── __init__.py
│   │   ├── base_dto.py          # Base DTO class
│   │   ├── customer_dto.py      # Customer DTO
│   │   ├── crop_dto.py          # Crop DTO
│   │   ├── extent_range_dto.py  # Extent Range DTO
│   │   ├── layout_dto.py        # Layout DTO
│   │   ├── payment_mode_dto.py  # Payment Mode DTO
│   │   ├── plot_dto.py          # Plot DTO

│   ├── schemas/                 # Pydantic models
│   │   ├── __init__.py
│   │   ├── customer_schema.py   # Customer schema

│   ├── daos/                    # Data Access Objects
│   │   ├── __init__.py
│   │   ├── customer_dao.py      # Customer DAO

├── .env                         # Environment variables
├── pyproject.toml               # Project configuration
└── Dockerfile (optional)        # Docker container setup
```

## Command to Run

```bash
ENV=local uvicorn main:app --reload --host 0.0.0.0 --port 8080
ENV=dev uvicorn main:app --reload --host 0.0.0.0 --port 8080
ENV=prod uvicorn main:app --reload --host 0.0.0.0 --port 8080
```

# KILL Ports
sudo lsof -i:8080
kill -9 <PID Number>

0. list customer -> done
1. list plots owned by customer -> done

2. list layouts -> done
3. list plots foreach layout -> done
4. list history foreach plot

5. list cops -> done
6. list pricing foreach crops -> done