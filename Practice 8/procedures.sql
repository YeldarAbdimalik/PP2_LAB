CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts
        SET phone = p_phone
        WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;

CALL upsert_contact('Ali', '12345');

CREATE OR REPLACE PROCEDURE delete_contact(p_value VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p_value OR phone = p_value;
END;
$$;

CALL delete_contact('Ali');

CREATE OR REPLACE PROCEDURE bulk_insert_contacts(
    names TEXT[],
    phones TEXT[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(names, 1)
    LOOP
        -- проверка: телефон только цифры
        IF phones[i] ~ '^[0-9]+$' THEN
            INSERT INTO contacts(name, phone)
            VALUES (names[i], phones[i]);
        ELSE
            RAISE NOTICE 'Invalid phone: % for %', phones[i], names[i];
        END IF;
    END LOOP;
END;
$$;

CALL bulk_insert_contacts(
    ARRAY['Ali', 'Bob'],
    ARRAY['12345', 'abc']
);