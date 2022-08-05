// This script creates the database connection using the pg module.
// pg should be installed with other dependencies listed in package.json .
import postgreSQL, { Pool } from 'pg';

const { pool } = postgreSQL;

export default (callback = null) => {
    const pool = new Pool({
        user: 'node',
        database: 'node',
        password: 'Cl@yt0n42!',
        host: 'localhost',
        port: 5432,
    });
};