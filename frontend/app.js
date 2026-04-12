const API_URL = 'http://localhost:8000/api';

document.addEventListener('DOMContentLoaded', () => {
    const isIndex = document.getElementById('hero-section') !== null;
    if (isIndex) initIndex();
    else initDashboard();
});

function initIndex() {
    const heroSection = document.getElementById('hero-section');
    const roleSelection = document.getElementById('role-selection');
    const loginSection = document.getElementById('login-section');
    
    if(localStorage.getItem('user')) {
        window.location.href = 'dashboard.html';
    }

    const homeBanner = document.getElementById('home-banner');

    document.getElementById('get-started-btn').addEventListener('click', () => {
        heroSection.classList.add('hidden');
        if(homeBanner) homeBanner.classList.add('hidden');
        setTimeout(() => {
            roleSelection.classList.remove('hidden');
        }, 50);
    });

    document.getElementById('back-to-hero').addEventListener('click', () => {
        roleSelection.classList.add('hidden');
        setTimeout(() => {
            heroSection.classList.remove('hidden');
            if(homeBanner) homeBanner.classList.remove('hidden');
        }, 50);
    });

    let currentRole = '';

    const activateRoleFlow = (roleClicked) => {
        currentRole = roleClicked;
        document.getElementById('auth-role').value = currentRole;
        document.getElementById('login-role-text').innerText = currentRole.charAt(0).toUpperCase() + currentRole.slice(1);
        
        if (currentRole === 'admin') {
            document.getElementById('auth-toggle').style.display = 'none';
            setAuthMode('login');
        } else {
            document.getElementById('auth-toggle').style.display = 'flex';
            setAuthMode('login');
        }

        heroSection.classList.add('hidden');
        roleSelection.classList.add('hidden');
        if(document.getElementById('home-banner')) document.getElementById('home-banner').classList.add('hidden');
        
        // Let CSS reset animation by briefly hiding logic
        loginSection.classList.add('hidden');
        setTimeout(() => {
            loginSection.classList.remove('hidden');
        }, 50);
    };

    document.querySelectorAll('.portal-nav').forEach(nav => {
        nav.addEventListener('click', (e) => {
            e.preventDefault();
            activateRoleFlow(e.currentTarget.dataset.role);
        });
    });

    document.querySelectorAll('.role-card').forEach(card => {
        card.addEventListener('click', (e) => {
            activateRoleFlow(e.currentTarget.dataset.role);
        });
    });

    document.getElementById('back-to-roles').addEventListener('click', () => {
        loginSection.classList.add('hidden');
        setTimeout(() => {
            roleSelection.classList.remove('hidden');
        }, 50);
    });

    // Auth Toggle logic
    document.querySelectorAll('.auth-tab').forEach(tab => {
        tab.addEventListener('click', (e) => {
            document.querySelectorAll('.auth-tab').forEach(t => t.classList.remove('active'));
            e.target.classList.add('active');
            setAuthMode(e.target.dataset.mode);
        });
    });

    function setAuthMode(mode) {
        document.getElementById('auth-mode').value = mode;
        const btn = document.getElementById('submit-btn');
        btn.innerText = mode === 'login' ? 'Login' : 'Sign Up';
        document.getElementById('auth-error').classList.remove('show');
        
        const container = document.getElementById('dynamic-fields');
        let html = '';

        if (mode === 'login') {
            const label = currentRole === 'admin' ? 'Username' : 'Email ID';
            const inputType = currentRole === 'admin' ? 'text' : 'email';
            
            html = `
                <div class="input-group">
                    <label>${label}</label>
                    <input type="${inputType}" name="identifier" required placeholder="Enter ${label.toLowerCase()}">
                </div>
                <div class="input-group">
                    <label>Password</label>
                    <input type="password" name="password" required placeholder="Enter password">
                </div>
            `;
        } else {
            // Sign up fields
            if (currentRole === 'faculty') {
                html = `
                    <div class="input-group"><label>Full Name</label><input type="text" name="name" required></div>
                    <div class="input-group"><label>Department</label><input type="text" name="department" required></div>
                    <div class="input-group"><label>Designation</label><input type="text" name="designation" required></div>
                    <div class="input-group"><label>Email ID</label><input type="email" name="email_id" required></div>
                    <div class="input-group"><label>Mobile Number</label><input type="text" name="mobile_number" required></div>
                    <div class="input-group"><label>Specialization</label><input type="text" name="area_of_specialization" required></div>
                    <div class="input-group"><label>Password</label><input type="password" name="password_hash" required></div>
                `;
            } else if (currentRole === 'student') {
                html = `
                    <div class="input-group"><label>Full Name</label><input type="text" name="name" required></div>
                    <div class="input-group"><label>Course Enrollment</label><input type="text" name="course_enrollment" required></div>
                    <div class="input-group"><label>Current Semester</label><input type="number" name="current_semester" required></div>
                    <div class="input-group"><label>Email ID</label><input type="email" name="email_id" required></div>
                    <div class="input-group"><label>Mobile Number</label><input type="text" name="mobile_number" required></div>
                    <div class="input-group"><label>Password</label><input type="password" name="password_hash" required></div>
                `;
            }
        }
        container.innerHTML = html;
    }

    document.getElementById('auth-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        const data = Object.fromEntries(formData.entries());
        const role = data.role;
        const mode = data.mode;
        const errorMsg = document.getElementById('auth-error');

        try {
            if (mode === 'login') {
                const res = await fetch(`${API_URL}/login`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ role, identifier: data.identifier, password: data.password })
                });

                const resData = await res.json();
                if (res.ok && resData.success) {
                    localStorage.setItem('user', JSON.stringify(resData.user));
                    localStorage.setItem('role', resData.role);
                    window.location.href = 'dashboard.html';
                } else {
                    errorMsg.innerText = resData.message || "Login failed";
                    errorMsg.classList.add('show');
                }
            } else {
                // Sign Up mode
                delete data.role;
                delete data.mode;
                delete data.identifier;
                
                const res = await fetch(`${API_URL}/${role}`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                
                if (res.ok) {
                    alert("Account created successfully! Please log in.");
                    document.querySelector('.auth-tab[data-mode="login"]').click(); // Switch to login
                } else {
                    errorMsg.innerText = "Error creating account. Information may already exist.";
                    errorMsg.classList.add('show');
                }
            }
        } catch (err) {
            errorMsg.innerText = "Server error. Is the Python backend running?";
            errorMsg.classList.add('show');
        }
    });

    // Make hero visible initially
    heroSection.classList.add('visible');
    heroSection.classList.remove('hidden');
}

function initDashboard() {
    const userStr = localStorage.getItem('user');
    const role = localStorage.getItem('role');

    if (!userStr || !role) {
        window.location.href = 'index.html';
        return;
    }

    const user = JSON.parse(userStr);
    document.getElementById('user-greeting').innerText = `Welcome, ${user.name || user.username || 'User'}`;

    document.getElementById('logout-btn').addEventListener('click', () => {
        localStorage.clear();
        window.location.href = 'index.html';
    });

    const contentArea = document.getElementById('content-area');
    const searchInput = document.getElementById('search-input');
    const title = document.getElementById('dashboard-title');
    const createBtn = document.getElementById('create-record-btn');

    if (role === 'student') {
        title.innerText = 'Student Profile';
        renderStudentProfile(user, contentArea);
    } else if (role === 'faculty') {
        title.innerText = 'Faculty Dashboard';
        searchInput.classList.remove('hidden');
        
        contentArea.innerHTML = `<div id="faculty-profile"></div><div class="mb-2"></div><div id="tables-wrapper"></div>`;
        renderFacultyProfile(user, document.getElementById('faculty-profile'));
        loadAndRenderTables(document.getElementById('tables-wrapper'), role, searchInput);

    } else if (role === 'admin') {
        title.innerText = 'Admin Dashboard';
        searchInput.classList.remove('hidden');
        createBtn.classList.remove('hidden');
        
        createBtn.addEventListener('click', () => {
            openCreateModal();
        });

        contentArea.innerHTML = `<div id="tables-wrapper"></div>`;
        loadAndRenderTables(document.getElementById('tables-wrapper'), role, searchInput);
    }
}

function loadAndRenderTables(container, role, searchInput) {
    let facultyData = [];
    let studentData = [];

    Promise.all([
        fetch(`${API_URL}/all/faculty`).then(res => res.json()),
        fetch(`${API_URL}/all/student`).then(res => res.json())
    ]).then(([fData, sData]) => {
        facultyData = fData.data;
        studentData = sData.data;
        
        const render = (q) => {
            const fFiltered = facultyData.filter(d => JSON.stringify(Object.values(d)).toLowerCase().includes(q.toLowerCase()));
            const sFiltered = studentData.filter(d => JSON.stringify(Object.values(d)).toLowerCase().includes(q.toLowerCase()));
            
            let html = `<h3 style="margin-bottom:1rem">Faculty Directory</h3><div class="table-container glass-panel"><table>
                <tr><th>Name</th><th>Department</th><th>Designation</th><th>Email</th><th>Mobile</th>${role === 'admin' ? '<th>Actions</th>' : ''}</tr>`;
            
            fFiltered.forEach(f => {
                html += `<tr>
                    <td>${f.name}</td><td>${f.department}</td><td>${f.designation}</td><td>${f.email_id}</td><td>${f.mobile_number}</td>`;
                if(role === 'admin') {
                    html += `<td>
                        <button class="secondary-btn" style="margin-right:0.5rem" onclick="openEditModal('faculty', '${f.faculty_id}', ${JSON.stringify(f).replace(/"/g, '&quot;')})">Edit</button>
                        <button class="secondary-btn" style="color:var(--danger); border-color:var(--danger);" onclick="deleteRecord('faculty', 'faculty_id', '${f.faculty_id}')">Delete</button>
                    </td>`;
                }
                html += `</tr>`;
            });
            html += `</table></div>`;

            html += `<h3 class="mt-2" style="margin-bottom:1rem">Student Directory</h3><div class="table-container glass-panel"><table>
                <tr><th>Name</th><th>Course</th><th>Semester</th><th>Email</th><th>Mobile</th>${role === 'admin' ? '<th>Actions</th>' : ''}</tr>`;
            
            sFiltered.forEach(s => {
                html += `<tr>
                    <td>${s.name}</td><td>${s.course_enrollment}</td><td>${s.current_semester}</td><td>${s.email_id}</td><td>${s.mobile_number}</td>`;
                if(role === 'admin') {
                    html += `<td>
                        <button class="secondary-btn" style="margin-right:0.5rem" onclick="openEditModal('student', '${s.student_id}', ${JSON.stringify(s).replace(/"/g, '&quot;')})">Edit</button>
                        <button class="secondary-btn" style="color:var(--danger); border-color:var(--danger);" onclick="deleteRecord('student', 'student_id', '${s.student_id}')">Delete</button>
                    </td>`;
                }
                html += `</tr>`;
            });
            html += `</table></div>`;
            
            container.innerHTML = html;
        };

        render(searchInput.value || "");

        searchInput.addEventListener('input', (e) => {
            render(e.target.value);
        });

    }).catch(err => {
        container.innerHTML = `<p class="error-msg show">Failed to load data.</p>`;
    });
}

function renderStudentProfile(user, container) {
    container.innerHTML = `
        <div class="profile-card glass-panel">
            <h2 class="mb-2">Your Details</h2>
            <div class="profile-item"><span class="profile-item-label">Name</span><span>${user.name}</span></div>
            <div class="profile-item"><span class="profile-item-label">Course</span><span>${user.course_enrollment}</span></div>
            <div class="profile-item"><span class="profile-item-label">Semester</span><span>${user.current_semester}</span></div>
            <div class="profile-item"><span class="profile-item-label">Email</span><span>${user.email_id}</span></div>
            <div class="profile-item"><span class="profile-item-label">Mobile</span><span>${user.mobile_number}</span></div>
        </div>
    `;
}

function renderFacultyProfile(user, container) {
    container.innerHTML = `
        <div class="profile-card glass-panel" style="margin: 0 0 2rem 0; max-width: 100%;">
            <div class="dashboard-header" style="margin-bottom:1.5rem">
                <h2 style="font-size:1.8rem">Your Profile</h2>
                <button class="secondary-btn" onclick='openEditModal("faculty", "${user.faculty_id}", ${JSON.stringify(user).replace(/"/g, '&quot;')}, true)'>Edit Contact Info</button>
            </div>
            <div class="profile-item"><span class="profile-item-label">Name</span><span>${user.name}</span></div>
            <div class="profile-item"><span class="profile-item-label">Dept</span><span>${user.department}</span></div>
            <div class="profile-item"><span class="profile-item-label">Email</span><span>${user.email_id}</span></div>
            <div class="profile-item"><span class="profile-item-label">Mobile</span><span>${user.mobile_number}</span></div>
        </div>
    `;
}

window.openCreateModal = () => {
    const modal = document.getElementById('modal');
    document.getElementById('modal-title').innerText = "Create New Record";
    const fieldsContainer = document.getElementById('modal-fields');
    
    // Add a select to choose Table (Faculty vs Student)
    fieldsContainer.innerHTML = `
        <div class="input-group">
            <label>Record Type</label>
            <select id="create-type" name="_type">
                <option value="faculty">Faculty</option>
                <option value="student">Student</option>
            </select>
        </div>
        <div id="create-dynamic-fields"></div>
    `;

    const dynamicFields = document.getElementById('create-dynamic-fields');
    const renderFields = (type) => {
        let html = '';
        if (type === 'faculty') {
            html = `
                <div class="input-group mt-1"><label>Name</label><input type="text" name="name" required></div>
                <div class="input-group mt-1"><label>Department</label><input type="text" name="department" required></div>
                <div class="input-group mt-1"><label>Designation</label><input type="text" name="designation" required></div>
                <div class="input-group mt-1"><label>Email</label><input type="email" name="email_id" required></div>
                <div class="input-group mt-1"><label>Mobile</label><input type="text" name="mobile_number" required></div>
                <div class="input-group mt-1"><label>Specialization</label><input type="text" name="area_of_specialization" required></div>
                <div class="input-group mt-1"><label>Password</label><input type="password" name="password_hash" required></div>
            `;
        } else {
            html = `
                <div class="input-group mt-1"><label>Name</label><input type="text" name="name" required></div>
                <div class="input-group mt-1"><label>Course Enrollment</label><input type="text" name="course_enrollment" required></div>
                <div class="input-group mt-1"><label>Semester</label><input type="number" name="current_semester" required></div>
                <div class="input-group mt-1"><label>Email</label><input type="email" name="email_id" required></div>
                <div class="input-group mt-1"><label>Mobile</label><input type="text" name="mobile_number" required></div>
                <div class="input-group mt-1"><label>Password</label><input type="password" name="password_hash" required></div>
            `;
        }
        dynamicFields.innerHTML = html;
    };
    
    // Default to faculty
    renderFields("faculty");

    document.getElementById('create-type').addEventListener('change', (e) => {
        renderFields(e.target.value);
    });

    modal.classList.remove('hidden');

    document.getElementById('modal-close').onclick = () => modal.classList.add('hidden');
    
    document.getElementById('modal-form').onsubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        const submitData = Object.fromEntries(formData.entries());
        const table = submitData._type;
        delete submitData._type;

        try {
            const res = await fetch(`${API_URL}/${table}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(submitData)
            });
            if(res.ok) {
                modal.classList.add('hidden');
                window.location.reload();
            } else {
                alert("Failed to create record. Verify details.");
            }
        } catch(err) {
            alert("Error connecting to server.");
        }
    };
}

window.openEditModal = (table, id, data, isSelfUpdate = false) => {
    const modal = document.getElementById('modal');
    document.getElementById('modal-title').innerText = "Edit Record";
    const fieldsContainer = document.getElementById('modal-fields');
    fieldsContainer.innerHTML = '';
    
    let allowedKeys = Object.keys(data).filter(k => k !== 'password_hash' && !k.endsWith('_id'));
    
    if (isSelfUpdate) {
        allowedKeys = ['mobile_number', 'email_id'];
    }

    allowedKeys.forEach(k => {
        fieldsContainer.innerHTML += `
            <div class="input-group" style="margin-bottom:0.5rem">
                <label>${k.replace(/_/g, ' ').toUpperCase()}</label>
                <input type="${k.includes('email') ? 'email' : 'text'}" name="${k}" value="${data[k] || ''}" required>
            </div>
        `;
    });

    modal.classList.remove('hidden');

    document.getElementById('modal-close').onclick = () => modal.classList.add('hidden');
    
    document.getElementById('modal-form').onsubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        const updateData = Object.fromEntries(formData.entries());
        
        try {
            const res = await fetch(`${API_URL}/update/${table}/${table}_id/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(updateData)
            });
            if(res.ok) {
                modal.classList.add('hidden');
                if(isSelfUpdate) {
                    const u = JSON.parse(localStorage.getItem('user'));
                    Object.assign(u, updateData);
                    localStorage.setItem('user', JSON.stringify(u));
                }
                window.location.reload();
            } else {
                alert("Failed to update.");
            }
        } catch(err) {
            alert("Error connecting to server.");
        }
    };
}

window.deleteRecord = async (table, idCol, idVal) => {
    if(!confirm("Are you sure you want to delete this record?")) return;
    try {
        const res = await fetch(`${API_URL}/delete/${table}/${idCol}/${idVal}`, {
            method: 'DELETE'
        });
        if(res.ok) {
            window.location.reload();
        }
    } catch(err) {
        alert("Failed to delete record.");
    }
}
